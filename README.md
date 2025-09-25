# ML-based-Depression-recognition-using-Twitter (X)
The aim of this project is to detect depression in people using social media and hence, analyze a user's behaviour on social media.

# Abstract

Today online social networking platforms are heavily used to send messages and express opinions on specific topics and their sentiments on them have increased rapidly from the last few years. Sometimes people post something that they are currently more sentimental towards it and by analyzing such post we can infer their mood. 
ML based depression recognition using social media data project is a study on posts made by the user on social platform and its data characteristics to help us understand the factors that can affect a person’s mood that can affect mental health. But, we focus on depression by analyzing the posts weighted values from a collection of thousands of Tweets and processing it through a ML classifier. This could help us to understand how use of words and user interest in such social platform could lead to depression and also enable the platform to classify such users as mentally depressed allowing users to approach for professional help. 

# Introduction

The aim of this document is to gather formal resources and proceed with the project Multi-kernel ML based depression recognition using Twitter, which provide a service to recognize depression in people. This report documents an engineering approach to the above project completion by addressing the problem and solving it in a methodical and professional manner. 
# Depression
Depression is an extremely common illness affecting people of all ages, genders, different socioeconomic groups and religions in India and all over the world. Globally, an estimated 
280 million people were affected by depression in 2022. Depression contributes to significant disease burden at national and global levels. At the individual and family level, depression leads to poor quality of life, causing huge social and economic impact. 

It is one of the two diagnostic categories that constitute common mental disorders (CMDs), the other being anxiety disorder. Both are highly prevalent across the population (hence they are considered “common”) and impact on the mood or feelings of affected persons. Depression includes a spectrum of conditions with episodes, illnesses and disorders that are often disabling in nature, vary in their severity (from mild to severe) and duration (from months to years) and often exhibit a chronic course that has a relapsing and recurring trajectory over time. 

# Objectives
We develop a framework for sentiment analysis of Twitter data based on supervised learning 
techniques. The main components of framework consist of: 
. i.A pre-processing that assists with refining the data collection. 
  ii.A supervised module that aims to identify the sentiment polarity in Twitter data and properly classify them into depressed or not depressed. 
Also, to develop a web page to handle and visualize various results we gather from the Twitter Sentiment Analyzer.

# Proposed Methodology

We use Figure Eight’s "Sentiment Analysis: Emotion in Text" dataset which contains labels for the emotional content of 40000 texts across 13 labels and then transform it into 2 classes of “depressed” and “non-depressed” distinguishing them by associating labels to either positive emotion or negative emotion. For example, anger is considered to be associated to depression and therefore is considered a negative emotion. We will be then intuitively or rather through research be making categories of these emotions. We will be subjectively making assumption that negative emotion leads to depression and therefore giving it as a depressed state having a 0 value and linking positive emotion to a non-depressed state having a value of 1. Thus, we obtain a binary classification problem. Additionally, we pre-process the text of the transformed dataset to remove stopwords, punctuations and numerical values to make it ideal for significant feature selection.For feature selection, TF-IDF has been used. For classification, Logistic regression, Multinomial Naive Bayes, Gausssian Naive Bayes, Decision tree has been used.

# Conclusions 

The classifiers trained on transformed emotion dataset were able to successfully discriminate between the tweets fetched using “depressed” and “happy” phrases with the highest accuracy of 95.6% in Multinomial Naive Bayes classifier. Moreover, live evaluation of a user’s tweet to find whether they are depressed or not can be done with the web application.
The above technique can be used to analyze a user’s behaviour based on his/her tweets over a period of time for further analysis. 

# Future work

1) Enabling the classifier to use images and videos as objects of code so that the accuracy can be increased. 
2) To built a classifier that accept Indian languages so that the user feels more comfortable with the platform. 
