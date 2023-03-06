# Objection-Engine-Rabbit-Worker
A worker for RabbitMQ that runs objection_engine tasks.

## Getting Started

### Prerequisites

 - Python 3
 - An AMQP broker. I personally use RabbitMQ
 - Everything included in [/objection_engine/Readme.md](https://github.com/LuisMayo/objection_engine/blob/main/README.md#prerequisites)

### Installing

1. Clone the repository

```
git clone --recursive https://github.com/LuisMayo/Objection-Engine-Rabbit-Worker
```
2. Install dependencies of this repo. Refer to [objection engine's install instructions](https://github.com/LuisMayo/objection_engine/blob/main/README.md#installing) for any problems you may encounter
``` bash
python -m pip install .
```

3. Start the project, either the `slow_queue` for the rendering queue or the `fast_queue` for faster operations like the music list
`python slow_queue.py`

## Contributing
Since this is a tiny project we don't have strict rules about contributions. Just open a Pull Request to fix any of the project issues or any improvement you have percieved on your own. Any contributions which improve or fix the project will be accepted as long as they don't deviate too much from the project objectives. If you have doubts about whether the PR would be accepted or not you can open an issue before coding to ask for my opinion
