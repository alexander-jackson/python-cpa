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

You can then run `src/cpa.py activities.json` to calculate the critical path
analysis variables and display them to the screen. The above example should
display the following table containing the different variables.

```
  name  es  ef  ls  lf  tf  ff
0    a   0   6   3   9   3   1
1    b   0   3   0   3   0   0
2    c   3   7   4   8   1   0
3    d   3   8   3   8   0   0
4    e   7  11   9  13   2   2
5    f   8  13   8  13   0   0
```
