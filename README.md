Toolbuilder

Databricks SQL Module - Personal thoughts


Mostrar la utilidad del modulo de SQL, cuales son las ventajas y desventajas

1. Es un modulo util para Data Analysts que corren queries ad-hoc. Potencial uso en consultores de EI que saben "tirar queries"
2. Posibilidad de descargar resultados de queries en excel.
3. Es posible crear charts para cada query y crear dashboards usando diferentes charts. 
4. Se puede descargar dashboard en PDF y descargar data de los charts en excel 
5. Se puede crear charts tipo Pivot Tables con dos clicks. 
6. Se pueden guardar las queries corridas y generar schedules.
7. Es posible generar alertas sobre resultados de queries

- Need more information on the serverless option

Todos estos puntos se encuentran en una UI muy sencilla de usar, sin necesidad de instalar nada. 
No es util para hacer dashboards ni DW muy potentes pero si es muy facil hacer cosas sencillas. 



Analytics stack - Where the industry is going? - Personal thoughts

- We have been seen companies trying to expand their products to compete with other companies. Example: Azure developing Azure Synapses (not DW) based on Spark to compete with Databricks. And in the same way Databricks building SQL module to compete with traditional DW tools. At some point in the future we may be seeing companies having everything in their own solution. 

- Nowadays, Databricks seems to be the best solution to implement ML algorithms in production using big datasets and low run times. 

- SQL and Python seems to be de-facto language for data transformation. 

- To kick-off an entire analytics solution from zero, industry seems to be working mainly on these tools, following ELT paradigm:
  - Fivetran: data ingestion and loading
  - dbt: Data modelling and scheduling
  - Snowflake: Data Warehouse and storage
  - Tableu/PowerBI/Looker for visualizations
  
- Interesting to see that you only need SQL as a programming language. The rest are no-code apps.   

- Azure, Snowflake are going into the "Lakehouse" concept proposed by Databricks to replace the current Data Warehouse paradigm. 
  
- Databricks come the scenario when an ML algorithm needs to be implemented.

- Where we see the value today in databricks? 
  - We can kick-off multiple clusters to run different procedures. Example: when you need to load ton of data without interruptin the current process


- Resources: 
- https://royalcyberinc.medium.com/synapse-serverless-sql-vs-databricks-serverless-sql-654f8e79319d
- https://www.youtube.com/watch?v=VLtq0eeHc14