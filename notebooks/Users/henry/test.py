# Databricks notebook source exported at Thu, 17 Sep 2015 22:56:31 UTC
1 + 1

# COMMAND ----------

sc.parallelize(range(1, 100)).count() + 1