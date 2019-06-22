import pandas as pd

def train_cats(df):
    '''
    this function is to help proveide categorical type (encoding) 
    for the categorical variables.

    # Arguments
    df : data frame that holds training data set 

    # Return
    it provide an inplace process to interpret categorical variables 
    '''
    for label, content in df.iteritems():
        if df[label].dtypes not in ['int', 'float64']:
            df[label] = content.astype('category').cat.as_ordered()

    
def applay_cats(df, trn):
    '''
    this function can be used to give a categorical type for df categorical variables
    using the same way of coding used in the trainging set.

    # Arguments
    df: data frame --test or validation data set 
    trn: data frame -- training data set 

    # Return

    '''
    for label, content in df.items():
        if trn[label].dtype.name == 'category':
            df[label] = pd.Categorical(content, categories=trn[label].cat.categories, ordered=True)

###################################################
def courses_one_hot_encodeing(Courses, df):
    st_courses = list(df['Courses'].str.split(', '))
    one_hot = dict()
    temp = []
    for course in Courses:
        for index_, list_ in enumerate(st_courses):
            if course not in list_:
                temp.append('0')
            else:
                temp.append('1')
        one_hot[course] = temp
        temp = []
    one_hot_df = pd.DataFrame(one_hot)
    df = df.drop('Courses', axis = 1)
    df = df.join(one_hot_df)
    return df
###################################################
def attribute_value_converter(student_df):
    '''
    this method converts attribute values from arbic to english
    
    # Arguments 
    student_df : data frame of students data 
    
    #Return
    '''
    
    student_df['FarHome'] = student_df['FarHome'].map(
        {"ايوه" : "Yes",
        "لا" : "No"})

    student_df['HasAJob'] = student_df['HasAJob'].map(
        {"ايوه" : "YesHJ",
        "لا" : "NoHJ"})

    student_df['FinantialLevel'] = student_df['FinantialLevel'].map(
        {"عالي" : "High",
        "متوسط" : "Average",
        "ضعيف" : "Low"})

    student_df['GroupsResources'] = student_df['GroupsResources'].map(
        {"اه، باخد منها محاضرات أحيانًا" : "Follow",
        "مش متابع والله" : "Avoide",})

    student_df['FrequentAbcense'] = student_df['FrequentAbcense'].map(
        {"اه" : "Yes",
        "لا" : "No"})

    student_df['ExtraActivities'] = student_df['ExtraActivities'].map(
        {"اه" : "YesXA",
        "لا" : "NoXA"})

    student_df['HealthProblems'] = student_df['HealthProblems'].map(
        {"اه" : "Yes",
        "لا" : "No"})

    student_df['ParentsHaveDegree'] = student_df['ParentsHaveDegree'].map(
        {"اه" : "Yes",
        "لا" : "No"})

    student_df['EnglishLevel'] = student_df['EnglishLevel'].map(
        {"لغتي التانية يا جدععع" : "Advanced",
        "متوسط" : "Intermediate",
        "ضعيف": "beginner"})

    student_df['StudentGuardian'] = student_df['StudentGuardian'].map(
        {"بابا" : "Father",
        "ماما" : "Mother",
         "الاتنين": "Both",
        "حد تاني" : "Other"})

    student_df['InvolvmentLevel'] = student_df['InvolvmentLevel'].map(
        {"ملتزم" : "High",
        "بحضر نص نص" : "Average",
        "مش بحضر": "Low"})
    
    return student_df 

def one_hot_encoding(features, df):
    for feature in features:
        one_hot = pd.get_dummies(df[feature])
        df = df.drop(feature, axis = 1)
        df = df.join(one_hot)
    return df
def numericalize(df):
    for n, c in df.items():
        if not is_numeric_dtype(c):
            df[n] = col.cat.codes
        