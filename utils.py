# put the given milliseconds into the format H:MM:SS:mmm
def format_time(milliseconds: int):
    return f"{milliseconds // 3_600_000}:{milliseconds // 60_000 % 60:0>2d}:{milliseconds // 1_000 % 60:0>2d}.{milliseconds % 1_000:0<3d}"
