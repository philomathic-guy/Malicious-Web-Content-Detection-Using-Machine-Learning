import joblib
import features_extraction
import sys


def main():
    url = sys.argv[1]

    features_test = features_extraction.main(url)

    clf = joblib.load('classifier/random_forest.pkl')

    pred = clf.predict(features_test)

    # Print the probability of prediction (if needed)
    # prob = clf.predict_proba(features_test)
    # print 'Features=', features_test, 'The predicted probability is - ', prob, 'The predicted label is - ', pred
    #    print "The probability of this site being a phishing website is ", features_test[0]*100, "%"

    if int(pred[0]) == 1:
        # print "The website is safe to browse"
        print("SAFE")
    elif int(pred[0]) == -1:
        # print "The website has phishing features. DO NOT VISIT!"
        print("PHISHING")

        # print 'Error -', features_test


if __name__ == "__main__":
    main()
