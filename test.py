import joblib, features_extraction, sys
url=sys.argv[1]
# url="www.google.com"
features_test=features_extraction.main(url)

clf = joblib.load('classifier/random_forest.pkl')

pred=clf.predict(features_test)
prob=clf.predict_proba(features_test)
print 'The predicted probability is - ', prob, 'The predicted label is - ', pred