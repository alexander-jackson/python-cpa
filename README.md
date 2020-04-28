# CPA

CPA is a Python program for dealing with Critical Path Analysis.

## Usage

Assume `activities.json` contains the following:

```json
{
	"activities": {
		"a" : {
			"duration": 6,
			"dependencies": []
		},
		"b" : {
			"duration": 3,
			"dependencies": []
		},
		"c" : {
			"duration": 4,
			"dependencies": ["b"]
		},
		"d" : {
			"duration": 5,
			"dependencies": ["b"]
		},
		"e" : {
			"duration": 4,
			"dependencies": ["a", "c"]
		},
		"f" : {
			"duration": 5,
			"dependencies": ["c", "d"]
		}
	}
}
```

You can then run `./cpa activities.json` to perform the Critical Path Analysis.

## License
[MIT](https://choosealicense.com/licenses/mit/)
