## Data Model
[Data Model](data_model.png)

## Implementation

* Lives in hydrate_model.py


## System Design
[High level illustration (Whimsical chart)](https://whimsical.co/CXwom5A4cHgERX74bCFWnk)

#### Notes on Data Transformation
* Since data is received monthly, an admin would automate processes for that data to drop (securely) to S3 so that hydration can begin.
* Scales well since each added transformation task is trivial to monitor.
* Authentication/security is important here since we don't want just anyone sending data to our S3 buckets.
* This admin owns all backend failure recovery.

#### Notes on Data Storage
* S3 & Redshift are inexpensive relative to the power they provide. Both together can support thousands of individual data sources and transformations
* Storing the data as closely to the way it came in makes debugging and data integrity issues easier to spot than if we front-load aggregated calculations into hydrate_model.py.
* Minimal failures should come from here since the data is prepared in the prior step.
* Authentication treated the same here as Data Transformation

#### Notes on Data Serving
* The frontend would start with selectors for genres and production companies. These selectors would allow users to choose one or many of each.
* The final two selectors would decide which metric is being aggregated and how (average budget, total revenue, etc).
* These selectors would be the base for a SQL Builder which spits out a query based on the selectors.
* This does add the need for SQL experts and analysts to maintain and keep things neat/according to spec, but with self serve data reporting I like the philosophy of 'Have as many eyes as possible on things' over 'Set and forget it.'
* All together, the four selectors form a 'question' which runs the built SQL on Redshift
* After running a 'question' and fetching data, Ideally offer raw data to download by the user as well as simple visualization for quick analyses
* Ideally lives in Looker, but can be engineered simply using a tornado server or similar
* Authentication/security less of a problem here due to lack of PII and 'on-rails' nature of building SQL queries based on selectors with limited choices.
