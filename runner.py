import ray

ray.init(num_gpus=1)

d = ray.put("example")
print(ray.get(x_id))  # "example"
