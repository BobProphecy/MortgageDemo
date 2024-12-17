from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mortgage_analytics.config.ConfigStore import *
from mortgage_analytics.udfs.UDFs import *

@instrument
def troubled_mortgages(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(((col("UPB_to_Value_Ratio") > lit(1)) & col("LoanStatus").isin(lit("90"), lit("REO"))))
