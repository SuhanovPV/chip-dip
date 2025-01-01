import os
import chip_dip
def abs_path_from_project(rel_path: str):
    return os.path.abspath(os.path.join(os.path.dirname(chip_dip.__file__),  '..', rel_path))