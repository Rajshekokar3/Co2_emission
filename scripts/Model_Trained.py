import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error,r2_score,accuracy_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
import pickle
import os
df=pd.read_csv("../data/co2_emissions_dataset.csv")
df=df.drop(["make","model"],axis=1)

LE=LabelEncoder()
#label encoder
for col in df.columns:
    if df[col].dtypes =="object":
        df[col]=LE.fit_transform(df[col])

print(df.columns)
#feature selection
X=df.drop("co2_emissions",axis=1)
Y=df["co2_emissions"]

#standard scaler
scaler=StandardScaler()
X=scaler.fit_transform(X)

X_train,x_test,Y_train,y_test=train_test_split(X,Y,train_size=0.8,random_state=42)

#modelbuilding
regression_models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Lasso Regression": Lasso(alpha=0.1),
    "ElasticNet Regression": ElasticNet(alpha=0.1, l1_ratio=0.5),
    "Decision Tree": DecisionTreeRegressor(max_depth=10, min_samples_split=4),
    "Random Forest": RandomForestRegressor(n_estimators=100, max_depth=10, min_samples_split=4, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=5),
    "Support Vector Regressor": SVR(kernel='rbf', C=100, epsilon=0.1),
    "K-Nearest Neighbors": KNeighborsRegressor(n_neighbors=5, weights='distance')
}
results=[]
best_model=None
best_score=-np.inf #initize with the lowset score

for name, model in regression_models.items():
    model.fit(X_train,Y_train)
    y_pred=model.predict(x_test)
    r2=r2_score(y_test,y_pred)
    mser=np.sqrt(mean_squared_error(y_test,y_pred))

    results.append((name,r2,mser))
    #Track the model
    if r2 > best_score:
        best_score=r2
        best_model=model

#result print
results_df=pd.DataFrame(results,columns=['Model','r2',"mser"])
result=results_df.sort_values(by="r2", ascending=False)
#selecting the best model
best_model_name=result.iloc[0]["Model"]
best_Model=regression_models[best_model_name]
print(f"Best Model {best_Model}")


#model saving
save_directory="D:\\Co2_emission_project\\models"
os.makedirs(save_directory, exist_ok=True)

model_path= os.path.join(save_directory,"best_model.pkl")
with open("best_model.pkl","wb") as file:
    pickle.dump(best_Model,file)

with open("scaler.pkl","wb") as file:
    pickle.dump(scaler,file)

print(f"Best model ({best_model_name}) saved successfully at: {model_path}")