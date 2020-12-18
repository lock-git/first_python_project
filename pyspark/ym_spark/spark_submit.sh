# 判断RegexFind.zip是否存在，如果存在删除
if [ -f "./RegexFind.zip" ]
then
    echo "RegexFind.zip exists"
    rm -f RegexFind.zip
fi

# 判断RegexFind是否存在，如果存在删除
if [ -d "./RegexFind" ]
then
    echo "RegexFind exists"
    rm -rf ./RegexFind
fi

# 重新复制RegexFind并且压缩成zip包
cp -r ../RegexFind ./
zip -r RegexFind.zip RegexFind/


export PYTHONIOENCODING=utf8
export SPARK_HOME=/usr/hdp/2.6.3.0-235/spark2
export PYTHONPATH=/opt/anaconda2/lib/python2.7/site-packages:$SPARK_HOME/bin:$SPARK_HOME/python:$SPARK_HOME/python/lib/pyspark.zip:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH




# local 模式启动
spark-submit --master local --jars /usr/hdp/2.6.3.0-235/hive-hcatalog/share/hcatalog/hive-hcatalog-core-1.2.1000.2.6.3.0-235.jar,/app/workdir/jar/mysql-connector-java-5.1.35-bin.jar --driver-class-path /app/workdir/jar/mysql-connector-java-5.1.35-bin.jar  --driver-memory 20G --executor-memory 2G --num-executors 20 execute_data_process_column.py



# yarn 模式启动
spark-submit --master yarn --queue kylin --jars /usr/hdp/2.6.3.0-235/hive-hcatalog/share/hcatalog/hive-hcatalog-core-1.2.1000.2.6.3.0-235.jar,/app/workdir/jar/mysql-connector-java-5.1.35-bin.jar --driver-class-path /app/workdir/jar/mysql-connector-java-5.1.35-bin.jar  --driver-memory 20G --executor-memory 2G --num-executors 100 execute_data_process_column.py



