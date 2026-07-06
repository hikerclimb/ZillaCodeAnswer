import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.functions._
import org.apache.spark.sql.expressions.Window
import org.apache.spark
import java.time._

val spark = SparkSession.builder().appName("run-spark-code").getOrCreate()

import spark.implicits._

def etl(input_df: DataFrame): DataFrame = {
	val currentYear = 2024
    val filtered_df = input_df.filter(
    $"view_count" > 1000000 && $"release_year" >= currentYear - 5
  )
  filtered_df
}