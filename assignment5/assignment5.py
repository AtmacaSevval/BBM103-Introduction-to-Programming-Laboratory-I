import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-0.005 * x))


def sigmoid_derivative(x):
    return 0.005 * x * (1 - x)


def read_and_divide_into_train_and_test(csv_file):
    data = pd.read_csv(csv_file)
    data.replace('?', 1, inplace=True)
    labels = data['Class']
    features = data.loc[:, 'Clump_Thickness':'Mitoses']
    train_pct_index = int(0.8 * len(data))
    training_inputs, training_labels = features[:train_pct_index], labels[:train_pct_index]
    test_inputs, test_labels = features[train_pct_index:], labels[train_pct_index:]
    data.replace('?', 1, inplace=True)
    data.drop(['Code_number'], 1, inplace=True)
    data.drop(['Class'], 1, inplace=True)
    data.Bare_Nuclei = np.array(data.Bare_Nuclei, dtype='int')
    f = plt.figure(figsize=(19, 15))
    plt.matshow(data.corr(), fignum=f.number)
    plt.xticks(range(data.shape[1]), data.columns, fontsize=14, rotation=90)
    plt.yticks(range(data.shape[1]), data.columns, fontsize=14, rotation=0)
    plt.imshow(data.corr(), interpolation='nearest')
    cb = plt.colorbar()
    data1=data.columns     
    for i in range(len(data1)):
        for j in range(len(data1)):
            plt.text(i,j,round(data.corr()[data1[i]][j],2),fontsize=10)    
    plt.show()
    return training_inputs, training_labels, test_inputs, test_labels


accuracy = 0
def run_on_test_set(test_inputs, test_labels, weights):
    tp = 0
    test_inputs = np.array(test_inputs, dtype='int')
    test_output = sigmoid(np.dot(test_inputs, weights))
    test_predictions = [[0]] * len(test_labels)
    for i in range(len(test_output)):
        if test_output[i] > 0.5:
            test_predictions[i] = [1]
        else:
            test_predictions[i] = [0]
    test_predictions = np.array(test_predictions)
    for predicted_val, label in zip(test_predictions, test_labels):
        if predicted_val == label:
            tp += 1
    global accuracy
    accuracy = tp / len(test_predictions)
    return accuracy


def plot_loss_accuracy(accuracy_array, loss_array):
    plt.plot(accuracy_array)
    plt.plot(loss_array)
    plt.xlabel('epoch')
    plt.legend(['Accuracy', 'Loss'])
    plt.show()


def main():
    csv_file = './breast-cancer-wisconsin.csv'
    iteration_count = 2500
    np.random.seed(1)
    weights = 2 * np.random.random((9, 1)) - 1
    accuracy_array = []
    loss_array = []
    training_inputs, training_labels, test_inputs, test_labels = read_and_divide_into_train_and_test(csv_file)

    for iteration in range(iteration_count):
        # calculate outputs
        training_inputs = np.array(training_inputs, dtype='int')
        outputs = np.dot(training_inputs, weights)
        outputs = sigmoid(outputs)
        # calculate loss
        training_labels = np.array(training_labels, dtype='int')
        training_labels = np.vstack(training_labels)
        loss = training_labels - outputs
        # calculate tuning
        tunings = loss * sigmoid_derivative(outputs)
        # update weights
        weights += np.dot(training_inputs.transpose(), tunings)
        run_on_test_set(test_inputs, test_labels, weights)
        accuracy_array.append([accuracy])
        loss_array.append(np.mean(loss))
    accuracy_array = np.array(accuracy_array)
    loss_array = np.array(loss_array)
    plot_loss_accuracy(accuracy_array, loss_array)


if __name__ == '__main__':
    main()
