
#!/usr/bin/python
import pandas as pd
import numpy as np
import pylab as pylab

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
#from sklearn import datasets
from sklearn import metrics
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

#from sklearn import datasets
#from sklearn import metrics
#from sklearn.linear_model import LogisticRegression

import numpy as np
import matplotlib.pyplot as plt

# an example graph type
def drawfig1(ylabels, xvalues, title=''):
    # create a new figure
    fig = plt.figure()

    # plot to it
    yvalues = np.arange(len(ylabels))
    plt.barh(yvalues, xvalues, figure=fig)
#    yvalues = 0.4
 #   plt.yticks(yvalues, ylabels, figure=fig)
    if title:
        plt.title(title, figure=fig)

    # return it
    return fig

from matplotlib.backends.backend_pdf import PdfPages

def write_pdf(fname, figures):
    doc = PdfPages(fname)
    for fig in figures:
        fig.savefig(doc, format='pdf')
    doc.close()

def drawfig(df, ttl=''):
	# Create a figure of given size
	fig = plt.figure(figsize=(16,12))
	# Add a subplot
	ax = fig.add_subplot(111)
	if ttl:
	        plt.title(ttl, figure=fig)

	# Set color transparency (0: transparent; 1: solid)
	a = 0.7
	# Create a colormap
	#customcmap = [(x/24.0,  x/48.0, 0.05) for x in range(len(df))]

	# Plot the 'population' column as horizontal bar plot
	df['Age'].plot(kind='barh', ax=ax, alpha=a, legend=False, 
                      edgecolor='w', xlim=(0,max(df['Age'])), title=ttl)
	return fig


'''
	for id in col_ids:
		if id != 'Name' and id != 'Sex' and id != 'Ticket' and id != 'Cabin' and id != 'Embarked':
			plt.subplot(plotval)
			print id
		    	traindf[id].plot()
			plotval = plotval+1
'''

def titanicdataexplore( traindf ):
	print "exploring the titanic data"
	print "plots"
	col_ids = list(traindf.columns.values)
	fig = plt.figure()	
	#host = fig1.add_subplot(111)
	#plotval = 111
	var = 'Age'
	traindf[var].plot()
	var = 'Fare'
	traindf[var].plot()


	#plt.hist(traindf.Fare, figure=fig1)
	#fig1 = traindf.Fare.hist(grid=False)
	#fig1.savefig('sumplot.pdf')	

	import matplotlib.backends.backend_pdf
	pdf = matplotlib.backends.backend_pdf.PdfPages("output.pdf")
	for fig in xrange(1, plt.figure().number): ## will open an empty extra figure :(
	    pdf.savefig( fig )
	pdf.close()
	#pylab.show()
	#a = drawfig(traindf, 'Agevssurvived')
	#b = drawfig(traindf.Sex, traindf.Survived, 'Sexvssurvived')
	#write_pdf('test.pdf', [fig1])

	print "end of data exploration"
	return 


import re


def fixagevar(traindf):
	
	master_vector = []
	miss_vector = []
	mrs_vector = []
	mr_vector = []
	dr_vector = []
	for i in range(1, len(traindf)):
	    match = (re.search(r'Master',  traindf['Name'].irow(i)))
	    if(match is not None):
		master_vector.extend([i])
	    match = (re.search(r'Miss',  traindf['Name'].irow(i)))
	    if(match is not None):
		miss_vector.extend([i])
	    match = (re.search(r'Mrs',  traindf['Name'].irow(i)))
	    if(match is not None):
		mrs_vector.extend([i])
	    match = (re.search(r'Mr',  traindf['Name'].irow(i)))
	    if(match is not None):
		mr_vector.extend([i])
	    match = (re.search(r'Dr',  traindf['Name'].irow(i)))
	    if(match is not None):
		dr_vector.extend([i])
		
		
	traindf['Namegroup'] = ""
	for i in master_vector:
	    traindf['Namegroup'].iloc[i] = "Master"
	for i in miss_vector:
	    traindf['Namegroup'].iloc[i] = "Miss"
	for i in mrs_vector:
	    traindf['Namegroup'].iloc[i] = "Mrs"    
	for i in mr_vector:
	    traindf['Namegroup'].iloc[i] = "Mr"    
	for i in dr_vector:
	    traindf['Namegroup'].iloc[i] = "Dr"       
	
	print "this is the value:"
	print traindf['Namegroup']
	
	master_age = traindf[traindf['Namegroup'] == "Master"]['Age'].dropna().mean()
	miss_age = traindf[traindf['Namegroup'] == "Miss"]['Age'].dropna().mean()
	mrs_age = traindf[traindf['Namegroup'] == "Mrs"]['Age'].dropna().mean()
	mr_age = traindf[traindf['Namegroup'] == "Mr"]['Age'].dropna().mean()
	dr_age = traindf[traindf['Namegroup'] == "Dr"]['Age'].dropna().mean()
	print "master age = ", master_age
	print "miss_age = ", miss_age
	print "mrs_age = ", mrs_age
	print "mr_age = ", mr_age
	print "dr_age = ", dr_age
	
	for i in range(1, len(traindf)):
	    if np.isnan(traindf['Age'][i]):
	        if (traindf['Namegroup'].iloc[i] == "Master"):
		    traindf['Age'][i] = master_age
		if (traindf['Namegroup'].iloc[i] == "Miss"):
		    traindf['Age'][i] = miss_age
		if (traindf['Namegroup'].iloc[i] == "Mrs"):
		    traindf['Age'][i] = mrs_age
		if (traindf['Namegroup'].iloc[i] == "Mr"):
		    traindf['Age'][i] = mr_age
		if (traindf['Namegroup'].iloc[i] == "Dr"):
		    traindf['Age'][i] = dr_age
		    
		    
	#print matchindex
	# create a new variable representing binned group
	# figure out how to round(mean(temptrainData$Age[temptrainData$Name == "Master"], na.rm = TRUE), digits = 2)
	# figure out how to if (temptrainData$Name[i] == "Master") {      trainData$Age[i] <- master_age }
	# figure out how to modify the original data frame
	
	print "Fill in missing age vars"
	print "form buckets"
	print "fill in values"
	return



def formtestandvalidationset(traindf):
    
	print "partition data"
	msk = np.random.rand(len(traindf)) < 0.8
	traindata = traindf[msk]
	validationdata = traindf[~msk]
	

	return 	(traindata, validationdata)


def model_diagnostics1(x_validation, y_prediction):
        C = confusion_matrix(x_validation,y_prediction)
        print C
        target_names = ["Survived", "Dead"]
        print classification_report(x_validation, y_prediction, target_names=target_names)
	#print accuracy_score(x_validation, y_prediction)
        plt.matshow(C)
        plt.title('Confusion matrix')
        plt.colorbar()
        plt.show()
	return 
    

def naivepredictionmodel(traindata,validationdata):
	print "everyone dies"
	x = 0
	columns = ['Survived']
	y = np.repeat(x, len(validationdata) , axis=0)
	indexnum = np.arange(0,len(validationdata),1)
	predictiondata = pd.DataFrame(columns=columns, index = indexnum)
	predictiondata['Survived'] = y
	#model_diagnostics1(validationdata['Survived'],predictiondata['Survived'])
	
	return 

def decisiontreemodel():
	print "decision tree model"
	return 
'''
import sklearn svm, linear_model

def logisticregressionmodel1():
        classifier = linear_model.LogisticRegression()
        # fit the model and make predictions:
	classifier.fit(data, targets)
	predict = classifier.predict(test_data)
        return
'''

def logisticregressionmodel(traindata,  validationdata):
    X = np.asarray(traindata)
    data = X[:,5]
    X = data.reshape(len(traindata), 1)
    print "this is X:"
    print X
    y = []
    for i in range(0, len(traindata)):
	y.extend([traindata['Survived'].iloc[i]])
    model = linear_model.LogisticRegression()
    model.fit(X, y)
    print "Fitted Logistic regression model:"
    print(model)
    # make predictions
    expected = validationdata['Survived']
    X = np.asarray(validationdata)
    data = X[:,5]
    X = data.reshape(len(validationdata), 1)
    predicted = model.predict(X)
    print "predicted output:"
    print predicted
    model_diagnostics1(expected,predicted)
    return 
	
    
def logisticregressionmodel2(traindata,  validationdata):
    # Logistic Regression
    
    #def data(filename):
    #X = pd.read_table(filename, sep=',', warn_bad_lines=True, error_bad_lines=True, low_memory = False)
    #X = pd.read_csv('train.csv', header=0)
    #X = np.asarray(traindata)
    data = X[:,4]
    X = data.reshape(len(traindata), 1)	
    #labels = X[:,1]
    print "this is X:"
    print X
    y = []
    for i in range(0, len(traindata)):
	y.extend([traindata['Survived'].iloc[i]])
    '''
    print "X"
    print X
    print "data"
    print data
    print "labels:"
    print np.unique(labels)
    #return data, labels
    '''	
    
   
    # fit a logistic regression model to the data
    model = linear_model.LogisticRegression()
    '''
  

    #The shape of X must be (n_samples, n_features) as explained in the SVC.fit docstring.
    #A 1-d array is interpreted as a single sample (for convenience when doing predictions on single samples).
    #Reshape your X to (n_samples, 1)
    train = traindata['Age'].values
    train = np.array(train)[:, np.newaxis]
    train = train.reshape(len(traindata), 1)	
    
    #X = np.array(traindata['Age']).reshape(len(traindata), 1)	
    #for i in range(1, len(traindata)):
    #X.extend([i, traindata['Age'].iloc[i]])
   
    print train
    print "Xshape = ", (train.shape)
     '''
    model.fit(X, y)
    print "Fitted Logistic regression model:"
    print(model)
    # make predictions
    expected = validationdata['Survived']
    predicted = model.predict(validationdata)
    # summarize the fit of the model
    #print(metrics.classification_report(expected, predicted))
    #print(metrics.confusion_matrix(expected, predicted))
    return 



def svmmodel(traindata,  validationdata):
    X = np.asarray(traindata)
    data = X[:,5]
    X = data.reshape(len(traindata), 1)
    print "this is X:"
    print X
    y = []
    for i in range(0, len(traindata)):
	y.extend([traindata['Survived'].iloc[i]])
    model = svm.SVC()
    model.fit(X, y)
    print "Fitted SVM  model:"
    print(model)
    # make predictions
    expected = validationdata['Survived']
    X = np.asarray(validationdata)
    data = X[:,5]
    X = data.reshape(len(validationdata), 1)
    predicted = model.predict(X)
    print "predicted output:"
    print predicted
    model_diagnostics1(expected,predicted)
    return
    

def randomforestmodel(traindata,  validationdata):
    X = np.asarray(traindata)
    data = X[:,5]
    X = data.reshape(len(traindata), 1)
    print "this is X:"
    print X
    y = []
    for i in range(0, len(traindata)):
	y.extend([traindata['Survived'].iloc[i]])
    forestmodel = RandomForestClassifier(n_estimators = 1000)
    forestmodel.fit(X, y)
    print "Fitted random forest  model:"
    print(forestmodel)
    # make predictions
    expected = validationdata['Survived']
    X = np.asarray(validationdata)
    data = X[:,5]
    X = data.reshape(len(validationdata), 1)
    predicted = forestmodel.predict(X)
    print "predicted output:"
    print predicted
    model_diagnostics1(expected,predicted)
    return    


def printmodeldiagnostics():
	print "model Diagnostics"
	return

def featureengineer():
	print "construct new variables"	
	return

def findmissingval(traindf):
	col_ids = list(traindf.columns.values)
	
	for id in col_ids:
		index_missing = traindf[id].isnull()
		if traindf[id].dtype == float or traindf[id].dtype == int:
		    NAlist = np.isnan(traindf[id])
		    print id, ": NA count = ", np.sum(NAlist),"/", NAlist.count()
		    
		print id, ": NULL or empty or NA  count = ", np.sum(index_missing), "/", index_missing.count()

#	frame2 = frame[index_missEthnic != True]
	return

def main():
    
	# load the iris datasets
        #dataset = datasets.load_iris()
	print "read train data"
	traindf = pd.read_csv('train.csv', header=0)


	import sys

	orig_stdout = sys.stdout
	f = file('trainstats.txt', 'w')
	sys.stdout = f
	print traindf.head()
	print "======================================="
	print "train data frame"
	print "======================================="
	print traindf
	print "======================================="
	print "typeof train data frame"
	print "======================================="
	print type(traindf)
	print "======================================="
	print "datatypes train data frame"
	print "======================================="
	print traindf.dtypes
	print "======================================="
	print "Info train data frame"
	print "======================================="
	print traindf.info()
	print "======================================="
	print "description Info train data frame"
	print "======================================="
	print traindf.describe()
	findmissingval(traindf)
	
	sys.stdout = orig_stdout
	f.close()

	print "read test data"
	testdf = pd.read_csv('test.csv', header=0)
	print testdf.head()

	orig_stdout = sys.stdout
	f = file('teststats.txt', 'w')
	sys.stdout = f
	print testdf.head()
	print "======================================="
	print "test data frame"
	print "======================================="
	print testdf
	print "======================================="
	print "typeof test data frame"
	print "======================================="
	print type(testdf)
	print "======================================="
	print "datatypes test data frame"
	print "======================================="
	print testdf.dtypes
	print "======================================="
	print "Info test data frame"
	print "======================================="
	print testdf.info()
	print "======================================="
	print "description Info test data frame"
	print "======================================="
	print testdf.describe()
	findmissingval(testdf)
	
	sys.stdout = orig_stdout
	f.close()

	titanicdataexplore(traindf)
	fixagevar(traindf)
	(traindata, validdata) = formtestandvalidationset(traindf)
	
	print "traindata len = ",len(traindata)
	print  "validation data len = ", len(validdata)
	
	naivepredictionmodel(traindata, validdata)
	

	#logisticregressionmodel(traindata, validdata)
	#svmmodel(traindata, validdata)
	randomforestmodel(traindata, validdata)
	decisiontreemodel()
	featureengineer()
	decisiontreemodel()
	print "final model"
	print "write output"
	return
	
if __name__ == "__main__":
    main()






	
