# Question Categories

## Questions that Map to Builtin Queries

## Questions that Count Vertices with a WHERE

```gsql
CREATE QUERY countVertices() FOR GRAPH MyGraph {
  SumAccum<INT> @@vertexCount;
  results = SELECT v FROM MyVertex:v
             WHERE v.some_attribute == "some_value"
             ACCUM @@vertexCount += 1;
  PRINT @@vertexCount;
}
```