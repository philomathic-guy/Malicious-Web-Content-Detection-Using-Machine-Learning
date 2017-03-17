import joblib, features_extraction

features_test=features_extraction.main()

clf = joblib.load('classifier/random_forest.pkl')

pred=clf.predict(features_test)
prob=clf.predict_proba(features_test)
print 'The predicted probability is - ', prob
print 'The predicted label is - ', pred