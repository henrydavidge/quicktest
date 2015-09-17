# Databricks notebook source exported at Thu, 17 Sep 2015 02:40:01 UTC
1 + 1

# COMMAND ----------

sc.parallelize(range(1, 100)).count()