"""
Implementation of verifiers.
"""

import codes

# Number of verifiers in each verifier card.
VERIFIER_CARD_SIZE: dict[int, int] = dict([
   (1, 2),
   (2, 3),
   (3, 3),
   (4, 3),
   (5, 2),
   (6, 2),
   (7, 2),
   (8, 4),
   (9, 4),
   (10, 4),
   (11, 3),
   (12, 3),
   (13, 3),
   (14, 3),
   (15, 3),
   (16, 2),
   (17, 4),
   (18, 2),
   (19, 3),
   (20, 3),
   (21, 2),
   (22, 3),
   (23, 3),
   (24, 3),
   (25, 3),
   (26, 3),
   (27, 3),
   (28, 3),
   (29, 3),
   (30, 3),
   (31, 3),
   (32, 3),
   (33, 6),
   (34, 3),
   (35, 3),
   (36, 3),
   (37, 3),
   (38, 3),
   (39, 6),
   (40, 9),
   (41, 9),
   (48, 9),
])

def check_1(code: codes.Code, option: int) -> bool:
    """Compares blue with 1"""
    match option:
        case 0:
            return code["blue"] == 1
        case 1:
            return code["blue"] > 1
    raise ValueError(f"Invalid option {option}")

def check_2(code: codes.Code, option: int) -> bool:
    """Compares triangle with 3."""
    match option:
        case 0:
            return code["triangle"] < 3
        case 1:
            return code["triangle"] == 3
        case 2:
            return code["triangle"] > 3
    raise ValueError(f"Invalid option {option}")

def check_3(code: codes.Code, option: int) -> bool:
    """Compares yellow with 3."""
    match option:
        case 0:
            return code["yellow"] < 3
        case 1:
            return code["yellow"] == 3
        case 2:
            return code["yellow"] > 3
    raise ValueError(f"Invalid option {option}")

def check_4(code: codes.Code, option: int) -> bool:
    """Compares square with 4"""
    match option:
        case 0:
            return code["square"] < 4
        case 1:
            return code["square"] == 4
        case 2:
            return code["square"] > 4
    raise ValueError(f"Invalid option {option}")

def check_5(code: codes.Code, option: int) -> bool:
    """Checks if triangle is even."""
    match option:
        case 0:
            return code["triangle"] % 2 == 0
        case 1:
            return code["triangle"] % 2 == 1
    raise ValueError(f"Invalid option {option}")

def check_6(code: codes.Code, option: int) -> bool:
    """Checks if square is even."""
    match option:
        case 0:
            return code["square"] % 2 == 0
        case 1:
            return code["square"] % 2 == 1
    raise ValueError(f"Invalid option {option}")

def check_7(code: codes.Code, option: int) -> bool:
    """Checks if circle is even"""
    match option:
        case 0:
            return code["circle"] % 2 == 0
        case 1:
            return code["circle"] % 2 == 1
    raise ValueError(f"Invalid option {option}")

def check_8(code: codes.Code, option: int) -> bool:
    """Counts the number of 1s."""
    match option:
        case 0:
            return code.count(1) == 0
        case 1:
            return code.count(1) == 1
        case 2:
            return code.count(1) == 2
        case 3:
            return code.count(1) == 3
    raise ValueError(f"Invalid option {option}")

def check_9(code: codes.Code, option: int) -> bool:
    """Checks number of 3s."""
    match option:
        case 0:
            return code.count(3) == 0
        case 1:
            return code.count(3) == 1
        case 2:
            return code.count(3) == 2
        case 3:
            return code.count(3) == 3
    raise ValueError(f"Invalid option {option}")

def check_10(code: codes.Code, option: int) -> bool:
    """Checks number of 4s."""
    match option:
        case 0:
            return code.count(4) == 0
        case 1:
            return code.count(4) == 1
        case 2:
            return code.count(4) == 2
        case 3:
            return code.count(4) == 3
    raise ValueError(f"Invalid option {option}")

def check_11(code: codes.Code, option: int) -> bool:
    """Compares blue with yellow."""
    match option:
        case 0:
            return code["blue"] < code["yellow"]
        case 1:
            return code["blue"] == code["yellow"]
        case 2:
            return code["blue"] > code["yellow"]
    raise ValueError(f"Invalid option {option}")

def check_12(code: codes.Code, option: int) -> bool:
    """Compares triangle with circle."""
    match option:
        case 0:
            return code["triangle"] < code["circle"]
        case 1:
            return code["triangle"] == code["circle"]
        case 2:
            return code["triangle"] > code["circle"]
    raise ValueError(f"Invalid option {option}")

def check_13(code: codes.Code, option: int) -> bool:
    """Compares square with circle."""
    match option:
        case 0:
            return code["square"] < code["circle"]
        case 1:
            return code["square"] == code["circle"]
        case 2:
            return code["square"] > code["circle"]
    raise ValueError(f"Invalid option {option}")

def check_14(code: codes.Code, option: int) -> bool:
    """Finds the smallest digit."""
    match option:
        case 0:
            return code["blue"] < min(code["yellow"], code["purple"])
        case 1:
            return code["yellow"] < min(code["blue"], code["purple"])
        case 2:
            return code["purple"] < min(code["blue"], code["yellow"])
    raise ValueError(f"Invalid option {option}")

def check_15(code: codes.Code, option: int) -> bool:
    """Checks which digit is the largest."""
    match option:
        case 0:
            return code["blue"] > max(code["yellow"], code["purple"])
        case 1:
            return code["yellow"] > max(code["blue"], code["purple"])
        case 2:
            return code["purple"] > max(code["blue"], code["yellow"])
    raise ValueError(f"Invalid option {option}")

def check_16(code: codes.Code, option: int) -> bool:
    """Checks if there is more even or odd digits."""
    num_evens = len([i for i in code if i % 2 == 0])
    num_odds = len([i for i in code if i % 2 == 1])

    match option:
        case 0:
            return num_evens > num_odds
        case 1:
            return num_evens < num_odds
    raise ValueError(f"Invalid option {option}")

def check_17(code: codes.Code, option: int) -> bool:
    """Checks number of even digits."""
    num_evens = len([i for i in code if i % 2 == 0])
    match option:
        case 0:
            return num_evens == 0
        case 1:
            return num_evens == 1
        case 2:
            return num_evens == 2
        case 3:
            return num_evens == 3
    raise ValueError(f"Invalid option {option}")

def check_18(code: codes.Code, option: int) -> bool:
    """Checks the parity of the sum of the digits."""
    match option:
        case 0:
            return sum(code) % 2 == 0
        case 1:
            return sum(code) % 2 == 1
    raise ValueError(f"Invalid option {option}")

def check_19(code: codes.Code, option: int) -> bool:
    """Compares the sum of blue and yellow with 6."""
    match option:
        case 0:
            return code["blue"] + code["yellow"] < 6
        case 1:
            return code["blue"] + code["yellow"] == 6
        case 2:
            return code["blue"] + code["yellow"] > 6
    raise ValueError(f"Invalid option {option}")

def check_20(code: codes.Code, option: int) -> bool:
    """Checks number of digit repetitions."""
    match option:
        case 0:
            return len(set(code)) == 3
        case 1:
            return len(set(code)) == 2
        case 2:
            return len(set(code)) == 1
    raise ValueError(f"Invalid option {option}")

def check_21(code: codes.Code, option: int) -> bool:
    """Checks if there is a digit that repeats twice."""
    match option:
        case 0:
            return len(set(code)) != 2  # either 3 different digits or just one
        case 1:
            return len(set(code)) == 2
    raise ValueError(f"Invalid option {option}")

def check_22(code: codes.Code, option: int) -> bool:
    """Checks if the digits are in a strictly monotonic order."""
    increasing = all(code[i] < code[i+1] for i in range(len(code)-1))
    decreasing = all(code[i] > code[i+1] for i in range(len(code)-1))
    match option:
        case 0:
            return increasing
        case 1:
            return decreasing
        case 2:
            return not increasing and not decreasing
    raise ValueError(f"Invalid option {option}")

def check_23(code: codes.Code, option: int) -> bool:
    """Compares the sum of the digits with 6."""
    match option:
        case 0:
            return sum(code) < 6
        case 1:
            return sum(code) == 6
        case 2:
            return sum(code) > 6
    raise ValueError(f"Invalid option {option}")

def check_24(code: codes.Code, option: int) -> bool:
    """Checks the length of the longest sequence of consecutive digits."""
    consecutive_pairs = [i for i in range(len(code)-1) if code[i+1] - code[i] == 1]
    match option:
        case 0:
            return len(consecutive_pairs) == 0
        case 1:
            return len(consecutive_pairs) == 1
        case 2:
            return len(consecutive_pairs) == 2
    raise ValueError(f"Invalid option {option}")

def check_25(code: codes.Code, option: int) -> bool:
    """Checks the length of the longest sequence of consecutive (increasing or decreasing)digits."""
    increasing_pairs = [i for i in range(len(code)-1) if code[i+1] > code[i]]
    decreasing_pairs = [i for i in range(len(code)-1) if code[i+1] < code[i]]
    match option:
        case 0:
            return len(increasing_pairs) == 0 and decreasing_pairs == 0
        case 1:
            return len(increasing_pairs) == 1 or decreasing_pairs == 1
        case 2:
            return len(increasing_pairs) == 2 or decreasing_pairs == 2
    raise ValueError(f"Invalid option {option}")

def check_26(code: codes.Code, option: int) -> bool:
    """Compares one of the digits with 3."""
    match option:
        case 0:
            return code[0] < 3
        case 1:
            return code[1] < 3
        case 2:
            return code[2] < 3
    raise ValueError(f"Invalid option {option}")

def check_27(code: codes.Code, option: int) -> bool:
    """Compares one of the digits with 4."""
    match option:
        case 0:
            return code[0] < 4
        case 1:
            return code[1] < 4
        case 2:
            return code[2] < 4
    raise ValueError(f"Invalid option {option}")

def check_28(code: codes.Code, option: int) -> bool:
    """Compares one of the digits with 1."""
    match option:
        case 0:
            return code[0] == 1
        case 1:
            return code[1] == 1
        case 2:
            return code[2] == 1
    raise ValueError(f"Invalid option {option}")

def check_29(code: codes.Code, option: int) -> bool:
    """Compares one of the digits with 3."""
    match option:
        case 0:
            return code[0] == 3
        case 1:
            return code[1] == 3
        case 2:
            return code[2] == 3
    raise ValueError(f"Invalid option {option}")

def check_30(code: codes.Code, option: int) -> bool:
    """Compares one of the digits with 4."""
    match option:
        case 0:
            return code[0] == 4
        case 1:
            return code[1] == 4
        case 2:
            return code[2] == 4
    raise ValueError(f"Invalid option {option}")

def check_31(code: codes.Code, option: int) -> bool:
    """Compares one of the digits with 1."""
    match option:
        case 0:
            return code[0] > 1
        case 1:
            return code[1] > 1
        case 2:
            return code[2] > 1
    raise ValueError(f"Invalid option {option}")

def check_32(code: codes.Code, option: int) -> bool:
    """Compares one of the digits with 3."""
    match option:
        case 0:
            return code[0] > 3
        case 1:
            return code[1] > 3
        case 2:
            return code[2] > 3
    raise ValueError(f"Invalid option {option}")

def check_33(code: codes.Code, option: int) -> bool:
    """Verifies the parity of one of the digits."""
    match option:
        case 0:
            return code[0] % 2 == 0
        case 1:
            return code[1] % 2 == 0
        case 2:
            return code[2] % 2 == 0
        case 3:
            return code[0] % 2 == 1
        case 4:
            return code[1] % 2 == 1
        case 5:
            return code[2] % 2 == 1
    raise ValueError(f"Invalid option {option}")

def check_34(code: codes.Code, option: int) -> bool:
    """Checks which digit is the smallest (not strictly)."""
    match option:
        case 0:
            return code[0] <= min(code[1], code[2])
        case 1:
            return code[1] <= min(code[0], code[2])
        case 2:
            return code[2] <= min(code[0], code[1])
    raise ValueError(f"Invalid option {option}")

def check_35(code: codes.Code, option: int) -> bool:
    """Checks which digit is the largest (not strictly)."""
    match option:
        case 0:
            return code[0] >= max(code[1], code[2])
        case 1:
            return code[1] >= max(code[0], code[2])
        case 2:
            return code[2] >= max(code[0], code[1])
    raise ValueError(f"Invalid option {option}")

def check_36(code: codes.Code, option: int) -> bool:
    """Checks if the sum of the digits is divisible by 3, 4, or 5."""
    match option:
        case 0:
            return sum(code) % 3 == 0
        case 1:
            return sum(code) % 4 == 0
        case 2:
            return sum(code) % 5 == 0
    raise ValueError(f"Invalid option {option}")

def check_37(code: codes.Code, option: int) -> bool:
    """Checks if the sume of some two digits is equal 4."""
    match option:
        case 0:
            return code[0] + code[1] == 4
        case 1:
            return code[0] + code[2] == 4
        case 2:
            return code[1] + code[2] == 4
    raise ValueError(f"Invalid option {option}")

def check_38(code: codes.Code, option: int) -> bool:
    """Checks if the sume of some two digits is equal 6."""
    match option:
        case 0:
            return code[0] + code[1] == 6
        case 1:
            return code[0] + code[2] == 6
        case 2:
            return code[1] + code[2] == 6
    raise ValueError(f"Invalid option {option}")

def check_39(code: codes.Code, option: int) -> bool:
    """Compares one of the digits with 1."""
    match option:
        case 0:
            return code[0] == 1
        case 1:
            return code[1] == 1
        case 2:
            return code[2] == 1
        case 3:
            return code[0] > 1
        case 4:
            return code[1] > 1
        case 5:
            return code[2] > 1
    raise ValueError(f"Invalid option {option}")

def check_40(code: codes.Code, option: int) -> bool:
    """Compares one of the digits with 3."""
    match option:
        case 0:
            return code[0] == 3
        case 1:
            return code[1] == 3
        case 2:
            return code[2] == 3
        case 3:
            return code[0] > 3
        case 4:
            return code[1] > 3
        case 5:
            return code[2] > 3
        case 6:
            return code[0] < 3
        case 7:
            return code[1] < 3
        case 8:
            return code[2] < 3
    raise ValueError(f"Invalid option {option}")

def check_41(code: codes.Code, option: int) -> bool:
    """Compares one of the digits with 4."""
    match option:
        case 0:
            return code[0] == 4
        case 1:
            return code[1] == 4
        case 2:
            return code[2] == 4
        case 3:
            return code[0] > 4
        case 4:
            return code[1] > 4
        case 5:
            return code[2] > 4
        case 6:
            return code[0] < 4
        case 7:
            return code[1] < 4
        case 8:
            return code[2] < 4
    raise ValueError(f"Invalid option {option}")

def check_48(code: codes.Code, option: int) -> bool:
    """Compares two digits against each other."""
    match option:
        case 0:
            return code[0] == code[1]
        case 1:
            return code[0] > code[1]
        case 2:
            return code[0] < code[1]
        case 3:
            return code[0] == code[2]
        case 4:
            return code[0] > code[2]
        case 5:
            return code[0] < code[2]
        case 6:
            return code[1] == code[2]
        case 7:
            return code[1] > code[2]
        case 8:
            return code[1] < code[2]
    raise ValueError(f"Invalid option {option}")


VERIFIER_CARDS = dict(
    (int(fn_name.split("_")[1]), fn)
    for fn_name, fn in locals().items() if fn_name.startswith("check_")
)
