from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

import argparse
import numpy as np
import pandas as pd
import pickle

header = ['p1_1', 'p1_2', 'p1_3', 'p1_4',
          'p2_1', 'p2_2', 'p2_3', 'p2_4',
          'p3_1', 'p3_2', 'p3_3', 'p3_4',
          'p4_1', 'p4_2', 'p4_3', 'p4_4',
          'winner']

def train(trainingData):
    print('Loading Training Dataset {0}'.format(trainingData))
    df = pd.read_csv(trainingData, names=header)
    gameStates = df.iloc[:, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]].values
    winners = df.iloc[:, -1].values

    print('Training RF')
    clf = RandomForestClassifier(n_jobs=2, max_depth=10)
    clf.fit(gameStates, winners)

    print('Feature Importances')
    print(clf.feature_importances_)
    return clf

def test(clf, testingData):
    print('Loading Testing Dataset {0}'.format(testingData))
    df = pd.read_csv(testingData, names=header)
    gameStates = df.iloc[:, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]].values
    winners = df.iloc[:, -1].values

    print('Evaluating RF')
    print(clf.score(gameStates, winners))

def save(clf, modelPath):
    print('Saving Model to {0}'.format(modelPath))
    pickle.dump(clf, open(modelPath, 'wb'))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trainingData', '-t', default='../datasets/basic/train.csv', help='file path to training data. defaults to ../datasets/basic/train.csv')
    parser.add_argument('--testingData', '-v', default='../datasets/basic/test.csv', help='file path to training data. defaults to ../datasets/basic/test.csv')
    parser.add_argument('--modelPath', '-m', default='models/basic.rf', help='file path to where model will be saved. defaults to models/basic.rf')

    args = parser.parse_args()
    clf = train(args.trainingData)
    test(clf, args.testingData)
    save(clf, args.modelPath)

if __name__ == "__main__":
    main()

