from typing import Dict, List


def getNextProbableWords(classes: List[Dict],
                         statements: List[str]) -> Dict[str, List[str]]:
  class_dict = {list(c.keys())[0]: list(c.values())[0] for c in classes}
  result = {}

  for statement in statements:
    keys = statement.split('.')
    current_dict = class_dict
    for key in keys[:-1]:
      current_dict = class_dict[current_dict[key]]

    last_key = keys[-1]
    if last_key == '':
      result[statement] = sorted([
        k for k in current_dict.keys() if isinstance(current_dict[k], str)
      ][:5])
    else:
      result[statement] = sorted([
        k for k in current_dict.keys()
        if k.startswith(last_key) and isinstance(current_dict[k], str)
      ][:5])

  return result
