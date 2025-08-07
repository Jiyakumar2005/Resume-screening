import pickle
from sklearn.preprocessing import LabelEncoder

# Replace this list with the actual categories used when training your model
labels = ['Data Science', 'HR', 'Advocate', 'Arts', 'Web Designing',
        'Mechanical Engineer', 'Sales', 'Health and fitness',
       'Civil Engineer', 'Java Developer', 'Business Analyst',
      'SAP Developer', 'Automation Testing', 'Electrical Engineering',
        'Operations Manager', 'Python Developer', 'DevOps Engineer',
       'Network Security Engineer', 'PMO', 'Database', 'Hadoop',
       'ETL Developer', 'DotNet Developer', 'Blockchain', 'Testing']

# Create and train the encoder
le = LabelEncoder()
le.fit(labels)

# Save the encoder to a file
with open('encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

print("✅ encoder.pkl created successfully.")
