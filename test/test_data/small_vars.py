correct_json_path = {
   "start":{
      "x":10,
      "y":22
   },
   "commands":[
      {
         "direction":"east",
         "steps":2
      },
      {
         "direction":"north",
         "steps":1
      },
   ]
}
correct_duplicate_json_path = {
   "start":{
      "x":10,
      "y":22
   },
   "commands":[
      {
         "direction":"east",
         "steps":2
      },
      {
         "direction":"west",
         "steps":1
      },
   ]
}
incorrect_json_path =  {
   "start":{
      "x":10,
      "y":22
   },
   "commands":[
      {
         "direction":"east",
         "steps":2
      },
      {
         "direction":"north"
      },
   ]
}
result_default_json = {
    "timestamp": "2023-01-01T01:01",
    "command": 2,
    "result": 4,
    "duration": 0.0008148193359375e-05
}
result_duplicate_vertex_json = {
    "timestamp": "2023-01-01T01:01",
    "command": 2,
    "result": 3,
    "duration": 0.0008148193359375e-05
}

result_heavy_json = {
  "timestamp": "2023-01-01T01:01",
  "command": 10000,
  "result": 204997,
  "duration": 0.0008148193359375e-05
}