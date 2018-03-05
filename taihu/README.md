# Table of Contents

- [20171031a](#20171031a)
- [20171113B](#20171113b)
- [20171113C](#20171113c)
- [20180301A](#20180301a)
- [](#)
- [](#)

```
get result/moea/taihu.json ./result/moea/
get result/moea/taihu.json.png ./result/moea/
```

# Grid, Delft3dWAQ, grid01-26

## 20170721a

cPickle, without decvar=0.0

tune 01 all

```
tuned_parameters = [{'solver': ['lbfgs','sgd','adam'],
					 'activation' : ['logistic', 'tanh', 'relu'],
					 'hidden_layer_sizes': [x for x in range(10,110,10)],
					 'batch_size' : [10,20,50,100,200],
					 'random_state' : [1,5,10]
					 }]
"grid01/taihu.json",
"grid02/taihu.json",
"grid10/taihu.json",
"grid11/taihu.json",
"grid12/taihu.json",
"grid13/taihu.json",
"grid21/taihu.json",
"grid22/taihu.json",
"grid23/taihu.json",
"grid24/taihu.json",
"grid25/taihu.json",
"grid26/taihu.json",
Mac: The scikit-learn version is 0.18.dev0. Before 20170721
gridALL
Best parameters set found on development set:
{'activation': 'relu', 'random_state': 5, 'batch_size': 10, 'solver': 'lbfgs', 'hidden_layer_sizes': 60}
Test-18 2.224826	6.782065
Predict 2.22091247306	6.75923620417
Score   0.0	0.999948337965
GridSearchCV(cv=None, error_score='raise',
	   estimator=MLPRegressor(activation='relu', solver='adam', alpha=0.0001,
	   batch_size=200, beta_1=0.9, beta_2=0.999, early_stopping=False,
	   epsilon=1e-08, hidden_layer_sizes=(100,), learning_rate='constant',
	   learning_rate_init=0.001, max_iter=200, momentum=0.9,
	   nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
	   tol=0.0001, validation_fraction=0.1, verbose=False,
	   warm_start=False),
	   fit_params={}, iid=True, n_jobs=1,
	   param_grid=[{'activation': ['logistic', 'tanh', 'relu'], 'random_state': [1, 5, 10], 'batch_size': [10, 20, 50, 100, 200], 'solver': ['lbfgs', 'sgd', 'adam'], 'hidden_layer_sizes': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}],
	   pre_dispatch='2*n_jobs', refit=True, scoring=None, verbose=0)
```

[_Back to TOC_](#table-of-contents)

## 20170721a

cPickle, without decvar=0.0

'mlmodel/d3d_ann_moea.pkl.20170721a'

tune 01 all

```
tuned_parameters = [{'solver': ['lbfgs','sgd','adam'],
					 'activation' : ['logistic', 'tanh', 'relu'],
					 'hidden_layer_sizes': [x for x in range(10,110,10)],
					 'batch_size' : [10,20,50,100,200],
					 'random_state' : [1,5,10]
					 }]
"grid01/taihu.json",
"grid02/taihu.json",
"grid10/taihu.json",
"grid11/taihu.json",
"grid12/taihu.json",
"grid13/taihu.json",
"grid21/taihu.json",
"grid22/taihu.json",
"grid23/taihu.json",
"grid24/taihu.json",
"grid25/taihu.json",
"grid26/taihu.json",
Mac:  The scikit-learn version is 0.18.1. After 20170721
gridALL
Best parameters set found on development set:
{'activation': 'relu', 'random_state': 5, 'solver': 'lbfgs', 'batch_size': 10, 'hidden_layer_sizes': 70}
Test-18 2.224826	6.782065
Predict 2.21987571269	6.76477696541
Score   0.0	0.999968858356
GridSearchCV(cv=None, error_score='raise',
	   estimator=MLPRegressor(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
	   beta_2=0.999, early_stopping=False, epsilon=1e-08,
	   hidden_layer_sizes=(100,), learning_rate='constant',
	   learning_rate_init=0.001, max_iter=200, momentum=0.9,
	   nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
	   solver='adam', tol=0.0001, validation_fraction=0.1, verbose=False,
	   warm_start=False),
	   fit_params={}, iid=True, n_jobs=1,
	   param_grid=[{'random_state': [1, 5, 10], 'activation': ['logistic', 'tanh', 'relu'], 'hidden_layer_sizes': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 'batch_size': [10, 20, 50, 100, 200], 'solver': ['lbfgs', 'sgd', 'adam']}],
	   pre_dispatch='2*n_jobs', refit=True, return_train_score=True,
	   scoring=None, verbose=0)
```

[_Back to TOC_](#table-of-contents)

tune 02 incremental learning "sgd"

```
tuned_parameters = [{'solver': ['sgd'],
					 'activation' : ['logistic', 'tanh', 'relu'],
					 'hidden_layer_sizes': [x for x in range(10,110,10)],
					 'batch_size' : [10,20,50,100,200],
					 'random_state' : [1,5,10]
					 }]
"grid01/taihu.json",
"grid02/taihu.json",
"grid10/taihu.json",
"grid11/taihu.json",
"grid12/taihu.json",
"grid13/taihu.json",
"grid21/taihu.json",
"grid22/taihu.json",
"grid23/taihu.json",
"grid24/taihu.json",
"grid25/taihu.json",
"grid26/taihu.json",
Mac: The scikit-learn version is 0.18.dev0. Before 20170721
gridSGD
Best parameters set found on development set:
{'activation': 'tanh', 'random_state': 5, 'batch_size': 10, 'solver': 'sgd', 'hidden_layer_sizes': 80}
Test-18 2.224826	6.782065
Predict 2.25521003748	6.62190527774
Score   0.0	0.997440891794
GridSearchCV(cv=None, error_score='raise',
	   estimator=MLPRegressor(activation='relu', solver='adam', alpha=0.0001,
	   batch_size=200, beta_1=0.9, beta_2=0.999, early_stopping=False,
	   epsilon=1e-08, hidden_layer_sizes=(100,), learning_rate='constant',
	   learning_rate_init=0.001, max_iter=200, momentum=0.9,
	   nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
	   tol=0.0001, validation_fraction=0.1, verbose=False,
	   warm_start=False),
	   fit_params={}, iid=True, n_jobs=1,
	   param_grid=[{'activation': ['logistic', 'tanh', 'relu'], 'random_state': [1, 5, 10], 'batch_size': [10, 20, 50, 100, 200], 'solver': ['sgd'], 'hidden_layer_sizes': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}],
	   pre_dispatch='2*n_jobs', refit=True, scoring=None, verbose=0)
```

[_Back to TOC_](#table-of-contents)

tune 02 incremental learning "sgd"

```
tuned_parameters = [{'solver': ['sgd'],
					 'activation' : ['logistic', 'tanh', 'relu'],
					 'hidden_layer_sizes': [x for x in range(10,110,10)],
					 'batch_size' : [10,20,50,100,200],
					 'random_state' : [1,5,10]
					 }]
"grid01/taihu.json",
"grid02/taihu.json",
"grid10/taihu.json",
"grid11/taihu.json",
"grid12/taihu.json",
"grid13/taihu.json",
"grid21/taihu.json",
"grid22/taihu.json",
"grid23/taihu.json",
"grid24/taihu.json",
"grid25/taihu.json",
"grid26/taihu.json",
Mac:  The scikit-learn version is 0.18.1. After 20170721
gridSGD
Best parameters set found on development set:
{'activation': 'tanh', 'random_state': 5, 'solver': 'sgd', 'batch_size': 20, 'hidden_layer_sizes': 30}
Test-18 2.224826	6.782065
Predict 2.2348922431	6.68759109001
Score   0.0	0.999130733513
GridSearchCV(cv=None, error_score='raise',
	   estimator=MLPRegressor(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
	   beta_2=0.999, early_stopping=False, epsilon=1e-08,
	   hidden_layer_sizes=(100,), learning_rate='constant',
	   learning_rate_init=0.001, max_iter=200, momentum=0.9,
	   nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
	   solver='adam', tol=0.0001, validation_fraction=0.1, verbose=False,
	   warm_start=False),
	   fit_params={}, iid=True, n_jobs=1,
	   param_grid=[{'random_state': [1, 5, 10], 'activation': ['logistic', 'tanh', 'relu'], 'hidden_layer_sizes': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 'batch_size': [10, 20, 50, 100, 200], 'solver': ['sgd']}],
	   pre_dispatch='2*n_jobs', refit=True, return_train_score=True,
	   scoring=None, verbose=0)
```

[_Back to TOC_](#table-of-contents)

# Grid, Delft3dWAQ, grid00, add decvar=0.0

## 20170721B

cPickle, without decvar=0.0

'mlmodel/d3d_ann_moea.pkl.20170721B'

```
tuned_parameters = [{'solver': ['lbfgs','sgd','adam'],
					 'activation' : ['logistic', 'tanh', 'relu'],
					 'hidden_layer_sizes': [x for x in range(10,110,10)],
					 'batch_size' : [10,20,50,100,200],
					 'random_state' : [1,5,10]
					 }]
"grid00/taihu.json",
"grid01/taihu.json",
"grid02/taihu.json",
"grid10/taihu.json",
"grid11/taihu.json",
"grid12/taihu.json",
"grid13/taihu.json",
"grid21/taihu.json",
"grid22/taihu.json",
"grid23/taihu.json",
"grid24/taihu.json",
"grid25/taihu.json",
"grid26/taihu.json",
gridALL
Best parameters set found on development set:
{'activation': 'tanh', 'random_state': 5, 'solver': 'lbfgs', 'batch_size': 10, 'hidden_layer_sizes': 70}
sklearn-clf
GridSearchCV(cv=None, error_score='raise',
	   estimator=MLPRegressor(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
	   beta_2=0.999, early_stopping=False, epsilon=1e-08,
	   hidden_layer_sizes=(100,), learning_rate='constant',
	   learning_rate_init=0.001, max_iter=200, momentum=0.9,
	   nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
	   solver='adam', tol=0.0001, validation_fraction=0.1, verbose=False,
	   warm_start=False),
	   fit_params={}, iid=True, n_jobs=1,
	   param_grid=[{'random_state': [1, 5, 10], 'activation': ['logistic', 'tanh', 'relu'], 'hidden_layer_sizes': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 'batch_size': [10, 20, 50, 100, 200], 'solver': ['lbfgs', 'sgd', 'adam']}],
	   pre_dispatch='2*n_jobs', refit=True, return_train_score=True,
	   scoring=None, verbose=0)
```

[_Back to TOC_](#table-of-contents)

* NSGA2, ANN, without decvar=0.0:
  20170721b, obj1_obj2
  
	```
    ngen=200&ndim=82&npop=100&nobj=2&ncon=0&cxpb=0.9
    run_moea_ann.py
    init_variable = samRandom(n=numVar)
    ind.fitness.values = Ynew_obj[0]
	```

* NSGA2, ANN, without decvar=0.0:
  20171030a, obj1_obj2
  
	```
    ngen=200&ndim=82&npop=100&nobj=2&ncon=0&cxpb=0.9
    run_moea_ann.py
    init_variable = 1.0
    ind.fitness.values = Ynew_obj[0]
	```

* NSGA2, ANN, without decvar=0.0:
  20171030b, obj1_obj2
  
	```
    ngen=200&ndim=82&npop=100&nobj=2&ncon=0&cxpb=0.9
    run_moea_ann.py
    init_variable = samRandom(n=numVar)
    ind.fitness.values = Ynew_obj[0]
	```

* NSGA2, Delft3dWAQ
  20171030c, obj1_obj2
  
	```
    ngen=1&ndim=82&npop=4&nobj=2&ncon=0&cxpb=0.9
    run_moea_d3d.py
    init_variable = samRandom(n=numVar)
    ind.fitness.values = Ynew_obj[0]
	```

* NSGA2, Delft3dWAQ
  20171030d, obj1_obj2
  
	```
    ngen=1&ndim=82&npop=4&nobj=2&ncon=0&cxpb=0.9
    run_moea_d3d.py
    init_variable = samRandom(n=numVar)
    ind.fitness.values = Ynew_obj[0]
	```

* NSGA2, Delft3dWAQ
  20171030e, obj1_obj2
  
	```
    ngen=1&ndim=82&npop=4&nobj=2&ncon=0&cxpb=0.9
    run_moea_d3d.py
    init_variable = samRandom(n=numVar)
    ind.fitness.values = Ynew_obj[0]
	```

* NSGA2, Delft3dWAQ
  **20171031a, obj1_obj2**
  
	```
    ngen=10&ndim=82&npop=40&nobj=2&ncon=0&cxpb=0.9
    run_moea_d3d.py
    init_variable = samRandom(n=numVar)
    ind.fitness.values = Ynew_obj[0]
	```

[_Back to TOC_](#table-of-contents)

# 20171031a

cPickle, without decvar=0.0

'mlmodel/d3d_ann_moea.pkl.20171031a'

```
tuned_parameters = [{'solver': ['lbfgs','sgd','adam'],
					 'activation' : ['logistic', 'tanh', 'relu'],
					 'hidden_layer_sizes': [x for x in range(10,110,10)],
					 'batch_size' : [10,20,50,100,200],
					 'random_state' : [1,5,10]
					 }]
"grid01/taihu.json",
"grid02/taihu.json",
"grid10/taihu.json",
"grid11/taihu.json",
"grid12/taihu.json",
"grid13/taihu.json",
"grid21/taihu.json",
"grid22/taihu.json",
"grid23/taihu.json",
"grid24/taihu.json",
"grid25/taihu.json",
"grid26/taihu.json",
'result/moea/20171030c-taihu.json',
'result/moea/20171030d-taihu.json',
'result/moea/20171030e-taihu.json',
'result/moea/20171031a-taihu.json',
gridALL
Best parameters set found on development set:
{'activation': 'relu', 'random_state': 10, 'solver': 'lbfgs', 'batch_size': 10, 'hidden_layer_sizes': 80}
sklearn-clf
GridSearchCV(cv=None, error_score='raise',
	   estimator=MLPRegressor(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
	   beta_2=0.999, early_stopping=False, epsilon=1e-08,
	   hidden_layer_sizes=(100,), learning_rate='constant',
	   learning_rate_init=0.001, max_iter=200, momentum=0.9,
	   nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
	   solver='adam', tol=0.0001, validation_fraction=0.1, verbose=False,
	   warm_start=False),
	   fit_params={}, iid=True, n_jobs=1,
	   param_grid=[{'random_state': [1, 5, 10], 'activation': ['logistic', 'tanh', 'relu'], 'hidden_layer_sizes': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 'batch_size': [10, 20, 50, 100, 200], 'solver': ['lbfgs', 'sgd', 'adam']}],
	   pre_dispatch='2*n_jobs', refit=True, return_train_score=True,
	   scoring=None, verbose=0)
```

[_Back to TOC_](#table-of-contents)

* NSGA2, ANN, without decvar=0.0:
  20171031b, obj1_obj2
  
	```
    ngen=200&ndim=82&npop=100&nobj=2&ncon=0&cxpb=0.9
    run_moea_ann.py
    init_variable = samRandom(n=numVar)
    ind.fitness.values = Ynew_obj[0]
	```

* NSGA2, Delft3dWAQ
  **20171101a, obj1_obj2**
  
	```
    ngen=2&ndim=82&npop=40&nobj=2&ncon=0&cxpb=0.9
    run_moea_d3d.py
    init_variable = samRandom(n=numVar)
    ind.fitness.values = Ynew_obj[0]
	```

[_Back to TOC_](#table-of-contents)

# 20171113B

cPickle, with decvar=0.0

'mlmodel/d3d_ann_moea.pkl.20171113B'

```
tuned_parameters = [{'solver': ['lbfgs','sgd','adam'],
					 'activation' : ['logistic', 'tanh', 'relu'],
					 'hidden_layer_sizes': [x for x in range(10,110,10)],
					 'batch_size' : [10,20,50,100,200],
					 'random_state' : [1,5,10]
					 }]
"grid00/taihu.json",
"grid01/taihu.json",
"grid02/taihu.json",
"grid10/taihu.json",
"grid11/taihu.json",
"grid12/taihu.json",
"grid13/taihu.json",
"grid21/taihu.json",
"grid22/taihu.json",
"grid23/taihu.json",
"grid24/taihu.json",
"grid25/taihu.json",
"grid26/taihu.json",
'result/moea/20171030c-taihu.json',
'result/moea/20171030d-taihu.json',
'result/moea/20171030e-taihu.json',
'result/moea/20171031a-taihu.json',
# 'result/moea/20171031b-taihu_cPickle.json',
'result/moea/20171101a-taihu.json',
gridALL
Best parameters set found on development set:
{'activation': 'relu', 'random_state': 5, 'solver': 'lbfgs', 'batch_size': 10, 'hidden_layer_sizes': 10}
sklearn-clf
GridSearchCV(cv=None, error_score='raise',
	   estimator=MLPRegressor(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
	   beta_2=0.999, early_stopping=False, epsilon=1e-08,
	   hidden_layer_sizes=(100,), learning_rate='constant',
	   learning_rate_init=0.001, max_iter=200, momentum=0.9,
	   nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
	   solver='adam', tol=0.0001, validation_fraction=0.1, verbose=False,
	   warm_start=False),
	   fit_params={}, iid=True, n_jobs=1,
	   param_grid=[{'random_state': [1, 5, 10], 'activation': ['logistic', 'tanh', 'relu'], 'hidden_layer_sizes': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 'batch_size': [10, 20, 50, 100, 200], 'solver': ['lbfgs', 'sgd', 'adam']}],
	   pre_dispatch='2*n_jobs', refit=True, return_train_score=True,
	   scoring=None, verbose=0)
```

[_Back to TOC_](#table-of-contents)

# 20171113C

priceTN, priceTP = 170.0, 1090.0 #euro/kg

'mlmodel/d3d_ann_moea.pkl.20171113B'

> Error: run_moea_ann.py [Xold_ind,Yold_obj,Xnew_ind,Ynew_obj], Don't use!

* NSGA2, ANN:
  20171113C, obj1_obj2
  
	```
    ngen=200&ndim=82&npop=100&nobj=2&ncon=0&cxpb=0.9
    run_moea_ann.py
    init_variable = samRandom(n=numVar)
    ind.fitness.values = Ynew_obj[0]
	```

* NSGA2, ANN:
  20171113C, obj1_obj3
  
	```
    ngen=200&ndim=82&npop=100&nobj=2&ncon=0&cxpb=0.9
    run_moea_ann.py
    init_variable = samRandom(n=numVar)
    ind.fitness.values = [Ynew_obj[0][0],obj3]
	```

* NSGA2, ANN:
  20171113C, obj2_obj3
  
	```
    ngen=200&ndim=82&npop=100&nobj=2&ncon=0&cxpb=0.9
    run_moea_ann.py
    init_variable = samRandom(n=numVar)
    ind.fitness.values = [Ynew_obj[0][1],obj3]
	```

[_Back to TOC_](#table-of-contents)

# 20180301A

priceTN, priceTP = 170.0, 1090.0 #euro/kg

'mlmodel/d3d_ann_moea.pkl.20171113B'

> Fix 20171113C error: run_moea_ann.py [Xold_ind,Yold_obj,Xnew_ind,Ynew_obj], Ok!

* NSGA2, ANN, cPickle:
  20180301A, obj12
  
	```
    ngen=200&ndim=82&npop=100&nobj=2&ncon=0&cxpb=0.9
    run_moea_ann.py
    init_variable = samRandom(n=numVar)
    population[ipop].fitness.values = [deepcopy(Y) for Y in [obj1,obj2]]
    get result/moea/taihu.json result/moea/20180301A-taihu_cPickle-obj12.json
    get result/moea/taihu.json.png result/moea/20180301A-taihu_cPickle-obj12.json.png
	```

* NSGA2, ANN, cPickle:
  20180301A, obj13
  
	```
    ngen=200&ndim=82&npop=100&nobj=2&ncon=0&cxpb=0.9
    run_moea_ann.py
    init_variable = samRandom(n=numVar)
    population[ipop].fitness.values = [deepcopy(Y) for Y in [obj1,obj2]]
    get result/moea/taihu.json result/moea/20180301A-taihu_cPickle-obj13.json
    get result/moea/taihu.json.png result/moea/20180301A-taihu_cPickle-obj13.json.png
	```

* NSGA2, ANN, cPickle:
  20180301A, obj23
  
	```
    ngen=200&ndim=82&npop=100&nobj=2&ncon=0&cxpb=0.9
    run_moea_ann.py
    init_variable = samRandom(n=numVar)
    population[ipop].fitness.values = [deepcopy(Y) for Y in [obj1,obj2]]
    get result/moea/taihu.json result/moea/20180301A-taihu_cPickle-obj23.json
    get result/moea/taihu.json.png result/moea/20180301A-taihu_cPickle-obj23.json.png
	```

[_Back to TOC_](#table-of-contents)
