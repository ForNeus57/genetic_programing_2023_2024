from typing import Tuple

input_values = Tuple[Tuple[int, ...], ...]

input_values = ((-81, 22, -37, -67, 63, 66, -61, 95, -87, -87), (16, -42, -35, 30, 67, -97, -83, 67, -26, 97), (61, 70, -43, 59, -51, -93, -8, 26, -40, -58), (-31, 8, 74, -63, -58, 40, 51, -63, 32, -78), (45, 69, -94, -78, -19, -42, -73, -61, -38, 97), (54, -39, -51, -31, 61, -52, 43, 96, -34, 4), (-57, 4, -38, -80, -55, -26, -50, 17, 49, -66), (-84, -54, 0, 42, -30, 10, 30, -73, 41, -38), (-69, -47, 5, 54, 77, 18, 51, -49, -3, 52), (62, -82, 74, -65, -86, 14, 50, 73, 81, 93), (69, 80, 56, 63, 34, -15, -73, -61, 13, 89), (-65, 10, 29, -51, 5, -35, 61, 80, -86, -93), (-62, -8, -2, 82, 39, 37, -39, -81, -65, 28), (17, 44, 71, 91, 54, -3, 88, -54, 73, 22), (72, 15, 95, -60, -67, -81, 57, -49, -95, 97), (39, 95, -79, 9, -69, 27, 25, -25, 52, 77), (64, -92, -60, 24, 3, -12, 62, 33, -94, -6), (23, -32, -13, 44, -99, -57, 41, 25, -35, -14), (66, 85, -22, 16, 35, -85, 53, 97, 45, -3), (36, -25, -81, 10, 89, 48, -41, -3, -71, -28), (50, -87, 23, -98, -1, 34, 27, -63, -53, 38), (-21, -20, 15, -13, 17, 15, 58, 88, 98, -69), (50, -8, 3, 50, 48, 36, -41, -23, -46, -4), (-30, -79, 58, -25, -76, 65, -28, 47, 20, -65), (90, -89, -59, -39, 91, 32, -18, 59, -25, 72), (-31, 13, 48, 70, -58, 52, -1, 64, -96, -26), (-1, -13, 35, 44, 33, 34, 34, 43, 39, -47), (-46, 59, 16, 88, 61, -60, -58, 67, 34, -51), (-28, -49, -64, -76, 4, -16, 73, 78, 1, -88), (1, -86, 44, -65, -25, -5, 2, 37, -13, -37), (47, -23, -77, -12, -39, 26, -79, 3, -74, -97), (54, 31, 30, -3, 61, 48, -48, -50, 76, 11), (41, 1, -44, -71, -95, 4, -41, 92, 29, 41), (-45, -55, -83, -50, 95, -77, -42, -80, 37, 31), (-2, 71, -62, 42, -85, -13, 49, 89, -24, -44), (21, -88, -38, 77, -58, 80, 43, 7, -40, 62), (-91, -19, 93, 11, -57, 70, 74, 96, 0, -32), (-90, 1, -72, -36, 51, 17, 91, 23, 96, -39), (-42, 24, -66, 7, 57, 39, -59, 70, -7, 76), (17, -87, 12, -98, -10, 86, -1, 30, -97, -32), (-46, -66, -81, 83, 92, -36, 94, -82, 38, -33), (-22, 62, -47, -60, -86, -4, 60, -62, 55, 63), (29, 79, 80, 96, 17, -19, 65, 79, 33, -90), (-74, 52, -52, 2, 83, 81, -12, -95, 29, 48), (53, -52, -2, -76, 67, 78, 18, 66, -66, 14), (86, -14, -12, 1, 22, 60, 29, -73, 86, 56), (40, 50, -43, 11, 33, 6, -4, 28, 50, -68), (64, -82, -14, -81, 96, 88, 9, -6, -29, 44), (-27, -41, 50, 73, -16, 14, 93, -58, -80, -31), (10, -87, 12, 47, -96, -82, 15, -24, -65, -58), (35, -3, 68, -84, 28, 8, 95, -60, 23, -35), (-59, 65, -84, -21, 10, 98, -63, 23, -33, -68), (-80, 57, -45, 99, -83, -68, -88, -32, 81, 29), (97, 64, -63, -64, 60, -7, 97, 25, 33, 40), (-51, -44, 59, 4, 56, 78, -21, 8, 99, -99), (26, 89, -82, 0, 54, -69, -76, 52, 83, 25), (-64, 97, 84, -78, -81, 89, -31, 0, 67, 89), (-76, 0, 88, 68, 64, 17, 74, 35, -3, 69), (50, -1, 45, -28, 40, -61, -17, 83, -31, 73), (-78, -95, 53, 29, 55, -21, -73, 20, -35, 16), (-2, -43, -70, -82, -72, 64, -19, 62, -18, -29), (-9, 21, 56, 93, -98, -45, 90, -91, 99, -37), (9, 18, 2, 61, -74, 66, -50, -24, -13, -51), (51, -24, 75, 65, 67, -2, 62, 2, -28, 29), (46, -80, -31, -32, 89, -19, -36, -62, -61, 98), (87, -2, -34, -52, 92, 32, 33, -79, -41, 84), (-80, 68, 64, -14, -11, -28, 85, 95, -82, -24), (92, -36, -65, -48, -69, 53, -79, -42, 20, 97), (16, 11, -60, -73, 91, 83, -75, 63, 1, -39), (-18, 38, -48, -81, 37, 5, 0, -1, 8, 33), (-41, -31, -13, -43, -69, -96, -7, -63, 6, -10), (-33, -96, -27, -33, 88, -59, 54, -96, 74, -5), (18, -62, 45, -86, -28, -70, 73, 78, -29, 57), (73, 97, -3, 67, 15, -69, 87, 35, 84, 19), (-87, -94, -88, 70, 64, -18, -37, -91, -22, 15), (66, -85, 97, 80, 74, 85, 26, 37, 21, -3), (-81, 37, 59, 78, -3, 52, -91, -14, 6, -73), (-55, -59, 45, -61, -26, 53, -30, -98, -53, 91), (34, 95, -18, 69, 56, 12, 97, -66, -63, -37), (-58, -68, -45, -4, 52, -42, -42, -65, 0, 94), (9, -85, 58, 69, -12, 42, 3, 45, -42, 6), (-82, -93, -3, -92, 52, -26, 71, 21, -25, -66), (-38, 75, 62, 14, 71, -56, 59, 32, 56, 8), (-93, 94, 41, 11, -3, 87, -51, 7, -24, 92), (15, 54, -86, -59, 14, -9, 75, -4, 45, 47), (-91, 34, -48, -48, -92, 66, 62, 98, -34, 35), (97, -82, -28, -99, 83, 15, 9, 94, 65, 28), (-67, 81, -49, 32, -40, 78, 2, -27, -54, 27), (-85, 72, -17, -65, -41, 11, 27, 65, -22, 9), (-28, 14, 47, 65, -40, -30, 91, -39, -58, -46), (-72, 61, -73, 55, 42, 3, -81, 60, -71, 94), (79, 38, -28, -46, -59, 86, -51, 80, 77, 68), (54, 54, 41, -33, 92, 92, -95, 66, 52, 7), (74, 19, 22, 67, 77, -40, -52, -75, 92, -36), (-18, 50, -66, 62, -74, -3, -97, 90, 98, 65), (11, 31, -91, 78, 27, 9, 95, -6, 35, 29), (65, 83, -74, 59, 54, -50, 73, -89, 35, -58), (0, -78, 10, 18, 1, 29, -42, -24, -13, 27), (-81, 98, -72, -77, -43, -71, 5, 12, -76, -29), (-14, -81, 28, 43, 45, 95, -98, 10, 78, -11), (45, 30, 43, 34, -70, 29, 55, -65, 33, -6), (46, 95, -2, -48, 8, 34, -79, -93, -94, -9), (53, 27, 89, 8, -15, 69, 11, 28, 43, 17), (24, -61, -94, 31, -25, 71, -50, 66, -81, -23), (-33, -16, 76, -1, -81, 39, 58, -60, -57, 21), (15, 62, 51, 47, 56, 82, 85, 98, -32, -72), (4, -29, 2, -22, 54, -95, 25, 32, 48, -62), (-42, 33, 88, 62, 1, 36, -41, 25, 53, -25), (-91, -62, 42, -80, 88, -42, 99, 48, 70, -68), (-95, -46, -46, -22, -20, -71, 15, -41, -27, 87), (-12, 35, -90, -67, -56, -13, 99, 2, 89, -46), (56, -89, -17, -89, 73, 8, 60, 87, 14, -1), (-19, 52, -39, 55, -41, -41, -12, -91, -15, 91), (86, 91, -77, 69, 25, -13, 50, 96, -22, -40), (72, 70, 91, -53, 57, -2, -63, -71, 76, 41), (-17, -63, 63, -95, 93, 8, -6, -75, 39, -56), (-78, -49, 25, -75, 17, -80, 87, -53, 54, 49), (14, -56, 56, -92, 14, -28, 16, -14, -87, -7), (-34, 6, 40, -1, -79, 53, 66, 93, -40, 96), (4, -76, -10, 38, 66, -56, -47, -99, 14, -12), (-44, 9, 80, -49, -3, 55, 14, 51, -13, -47), (-86, 57, 89, 17, 91, 12, -12, -41, -28, 29), (-84, -52, -32, -62, 41, -30, 48, -91, 85, -66), (-88, 28, 28, -80, 9, -25, 29, -79, 83, 96), (38, -19, 14, 3, -75, -96, -18, -42, 86, -47), (96, -92, -75, 32, -77, -32, 10, 56, 50, 58), (-35, -35, -17, -98, -81, 36, 48, 64, 70, 81), (61, 26, 18, 68, 93, -78, 5, -95, 44, -96), (86, 3, 67, 84, 69, -86, -11, -96, 82, 99), (31, -54, -13, 20, -41, -66, -12, 19, -95, 39), (-9, -23, 49, 39, 49, -18, 79, -20, 32, 63), (31, -49, -31, 97, -92, 15, 90, -5, 32, -80), (-31, -32, 40, -12, -11, 97, -28, -12, 32, -72), (70, -73, 77, -98, 81, -85, -20, 27, -50, 87), (77, -33, 69, -51, 8, 32, 74, 31, -64, -41), (-4, -60, -23, 86, -94, -91, 7, -46, -90, -94), (32, 50, 86, 90, 28, 40, -55, 18, 32, 96), (-10, 6, 70, 81, 4, 21, -52, 41, 61, -85), (10, 90, 52, -79, 36, -37, -26, -94, -26, 49), (-79, -51, 54, 51, -52, 9, -21, 39, 39, -21), (-65, -44, -31, 28, 54, 65, -63, -54, -79, -19), (-96, -73, -93, 24, 78, 96, -95, 10, -49, 22), (38, -96, 54, -90, 89, 52, 87, 49, 28, -95), (-94, -49, 70, -20, 59, 65, 4, 19, -29, -73), (-35, 33, 52, -75, 64, 13, 32, 20, -80, 37), (89, -72, 35, 69, -70, -30, -91, 39, 33, -89), (-92, -97, 95, 92, -81, -93, 41, -21, -51, -35), (54, -15, 72, 24, 79, -31, -90, -72, 42, 36), (-71, 2, 38, 13, 98, 47, -38, 14, -29, -41), (-6, 30, -70, 82, -94, 67, -31, -84, 42, 98), (-88, -96, 88, 38, 39, -6, 67, -47, -12, 59), (-77, 6, 3, -6, -85, 37, 86, 2, -41, -76), (31, 3, -79, -59, 36, -2, 62, -40, 3, 41), (25, 24, -26, -60, -12, 18, -59, -56, -23, 34), (16, -89, 44, -61, -85, -58, 38, -83, -40, -82), (4, 16, -66, -99, -95, -7, 74, 81, 57, 5), (3, 27, 51, -78, 52, 9, 16, -13, -92, 26), (-19, 44, 46, 41, -25, 4, -87, -78, -32, -23), (44, 46, 73, 69, -93, -53, -10, 39, -13, 18), (66, -96, -78, 78, 1, -80, 64, -22, -85, -7), (-36, -10, 18, 52, 65, -82, 54, 51, -14, -29), (-74, 86, -4, 39, 81, 8, -84, 95, -29, -31), (96, -27, 97, -8, 49, -76, 10, 32, -80, -99), (61, -25, -12, -20, 15, 37, 95, 53, -39, -24), (95, -39, 34, -54, -53, 27, 47, 27, 65, -5), (-57, -26, 18, -30, -28, 53, -50, 96, -88, -24), (-99, -86, 20, 7, -82, -73, 40, 38, -59, 37), (16, 27, 41, -42, -47, 21, 35, -14, -98, 12), (49, -61, 41, -17, 63, -98, -50, 8, -98, 88), (48, 29, 26, -29, 34, -45, -66, 44, -75, 5), (-54, -60, -77, 92, -11, -41, -20, -20, 9, 50), (-59, -31, 72, -33, -42, -93, -76, -26, -47, -85), (-13, -90, 68, 48, 55, -42, 52, 22, -15, 89), (8, 85, -62, -6, -7, 67, 80, -42, -33, -4), (34, -29, 52, 24, 55, 52, -22, -14, 85, -70), (-87, 36, 34, -99, 76, -98, -90, 24, -58, 79), (-36, 45, -95, -90, 75, 41, -42, -92, 76, 27), (81, -43, -12, -8, -72, 65, 98, -34, 45, 25), (73, -96, 97, -9, -17, -19, 63, 95, -50, -60), (-35, 88, 45, 29, -36, 1, -39, -87, 79, 51), (-31, 44, -45, -83, -4, 24, -53, 10, -95, -51), (-62, -4, 61, 33, 65, -56, 53, -51, -21, 46), (5, -95, -19, -72, -67, -12, 16, 8, 86, -15), (51, -7, 9, 92, -91, 70, -91, -47, -71, 61), (-26, -92, -94, 52, 95, -10, -47, -28, 12, -74), (53, -23, 35, 63, 31, -94, -73, -19, -68, -53), (33, 19, 66, -10, 50, 66, 98, 54, -12, 20), (-27, -50, -10, -38, -75, 36, 32, 43, 11, -3), (64, 61, 78, 85, 59, -73, 47, -5, -38, 18), (-18, 23, 69, -30, 64, -7, -90, -35, 48, 48), (31, -96, 21, 83, -88, -52, 83, 36, 15, 97), (-17, -23, 42, 1, -16, -59, 87, 8, 31, -52), (-81, 16, 60, 50, -12, -15, 49, -56, -95, 78), (17, -1, 68, 44, -70, -82, -34, -67, 7, 93), (10, 27, -52, -62, -54, -17, -2, -95, 97, -53), (62, -85, 70, 85, 16, -96, 44, 32, -69, 84), (62, 19, -23, -59, 71, -20, 46, -91, -69, -84), (-2, 21, 39, -58, -63, -68, -28, 59, 28, 93), (-20, -58, -49, 5, 26, 6, 67, 25, 68, 19), (-41, 63, 55, 47, 97, -32, 9, 76, 16, -51), (76, 92, -70, 95, 92, -92, 36, -99, -77, 80), (-1, -73, -90, 49, -22, 61, 78, 30, -5, 83), (-58, 58, 82, -10, -82, -15, 33, 39, -39, 55), (3, 96, -3, -45, 59, 3, 30, -27, -19, -76), (-45, 8, -6, 12, 50, -93, -21, -75, -66, -91), (-62, 96, -71, -86, -77, 81, -72, -35, -72, 15), (26, 91, 9, -90, -44, -65, 66, -83, -46, 14), (41, -7, 86, -91, -43, -56, 1, -60, -39, -92), (23, -24, -91, -20, -44, 19, -83, 94, -80, -81), (89, -48, -46, -3, 46, 14, 82, 49, 42, -5), (-4, -6, 85, -74, -13, 82, -57, -49, -72, -96), (51, -69, 48, 47, 81, 72, -29, -41, -88, 23), (7, -22, -45, 61, -77, -71, -70, -3, 85, 96), (91, 36, 75, -73, 27, -59, 2, 95, -45, -11), (60, -72, -63, 54, 16, 29, -18, -9, 92, -17), (71, -84, 29, -34, 9, 79, 42, 18, 15, 60), (60, -10, -92, 58, 18, 37, 3, 99, 84, 20), (-4, 89, -62, -54, -83, 70, 13, -97, -18, -95), (-52, -64, 91, 60, 98, 19, 0, 69, 61, -40), (59, -3, 48, -88, -63, 88, -52, -45, -14, 96), (49, -86, 12, 24, 30, -7, 88, 53, -16, -1), (-64, 24, -56, 75, -59, 91, -90, 52, 99, 37), (-38, 31, -57, 27, 51, 14, 54, -1, -49, 89), (54, -53, -93, -58, -70, -83, -71, -17, 94, -76), (-58, -5, 99, 64, 15, 26, 30, -29, 6, 86), (25, 11, 18, -63, 41, -21, 36, 14, 94, -54), (-35, -16, 58, -94, 86, -15, -20, -99, 41, -85), (61, -60, -99, 44, -16, 1, 99, 87, -82, 4), (-16, 49, 80, -70, 28, -44, 16, 56, 10, -88), (26, 54, 99, 68, -94, 27, 43, -53, -41, 39), (-7, 55, -29, -47, -33, 86, -84, 65, 69, 23), (-87, -30, 27, 69, -64, 33, -84, -72, -61, 45), (14, -44, 12, -48, 12, -56, -86, -82, -89, 87), (32, -71, -84, -28, 8, 37, -99, -97, 16, -64), (-45, -41, 76, 55, 63, -75, 62, -59, -41, 15), (50, -35, 84, 78, -93, -81, -72, 85, -70, 42), (-54, 55, -82, 94, 55, -99, -91, 28, 92, 64), (-59, 1, -73, -34, 84, -61, 78, 62, 20, 68), (-41, 95, -85, -49, -86, -40, 69, -88, 13, 37), (-40, -19, -52, -82, -8, -76, -61, 22, 49, 14), (44, -61, 32, -44, 25, 41, -12, 3, -84, -5), (-57, -21, -82, -1, 78, -37, 76, -85, 1, -78), (-5, 86, -84, -44, 9, 0, -49, 97, 69, 78), (50, 52, -62, -83, 95, 24, 67, -84, 11, 37), (85, -10, 46, -86, -76, 30, 36, -4, 80, -99), (26, 91, -12, -61, 57, 63, -26, 83, -47, 11), (-86, 4, 42, -31, -61, -36, -96, -75, 61, 44), (71, -59, 96, 24, 54, 19, 67, 44, 92, -75), (16, 97, 41, 84, 94, -78, 5, -18, 50, 86), (11, -81, 17, 97, -33, -28, 90, 50, 71, -3), (-25, 28, -79, 71, 3, 25, -84, 63, -5, -8), (90, 20, 15, -92, -53, -14, -72, -61, -34, 23), (-86, 96, -13, 44, 90, 21, -44, 67, 84, 78), (57, -12, -8, 85, -86, 32, -93, 62, 48, 51), (-50, -92, 29, -14, -92, -1, -20, -66, 22, -64), (79, 18, 77, 39, -36, -79, -90, 30, 96, 38), (-84, -74, -42, -67, -17, -30, -3, -25, -79, -15), (-4, 5, -78, 55, 31, -47, 67, -31, 62, -51), (47, 32, 2, -90, -15, 7, 60, -3, -51, 58), (53, 52, 35, -61, -23, -68, 65, -31, 96, 77), (-54, -76, -40, -23, -82, 26, 33, -54, -98, -12), (63, -98, 65, 38, 9, 50, 36, -79, -92, 73), (-34, -7, -93, -63, -47, 14, -43, 2, 48, -66), (46, -70, -51, 59, 32, 73, 95, -2, 62, 6), (51, -68, 7, 89, 68, -91, 13, -33, 95, -80), (-68, 36, 79, 93, -84, 89, -16, -25, 38, 95), (-33, -1, -35, -99, -29, 34, -70, 30, -39, 84), (80, -65, 3, 96, 27, 18, -96, 8, 11, 70), (67, 48, 66, 47, -90, -83, 55, 97, 41, 92), (76, 11, 99, 98, -71, -47, -95, 19, 92, -60), (30, -33, 22, 97, -56, 99, -39, -99, 34, 7), (57, -36, -7, -37, -62, -41, -59, 89, 47, -69), (-61, 3, 92, 45, 88, 65, -39, -73, -70, 6), (31, -17, -72, 8, 18, 54, 5, 97, -17, -8), (65, -79, -38, -66, 74, 97, 59, 78, 29, -77), (59, -73, -14, -48, 71, 22, 93, 95, -30, -42), (-26, -59, 18, 55, 95, 87, 12, -6, -78, -35), (48, 44, 83, -41, -44, 47, -69, 90, -78, -98), (76, 72, -40, -45, 91, -1, 17, 58, 10, -62), (-97, 95, 50, -67, 86, 12, 7, 60, -25, 19), (-48, 43, -48, -58, -20, -57, 4, -39, 3, 57), (84, 62, -50, -15, 13, -37, 56, -6, 18, 19), (-42, -64, 63, -17, -42, 38, -85, 67, 71, 68), (-93, -76, 50, 98, 22, -88, -58, -34, -68, 27), (-24, 91, -8, 77, -89, -63, -39, -70, 69, 90), (16, 23, 65, 78, 18, 37, -85, 25, 49, 20), (-99, 12, 72, 14, -11, -95, 40, -25, -65, 58), (-68, 33, 80, -88, 31, 19, 9, 45, -87, 4), (-92, 70, -49, -41, 88, -25, 73, -43, -98, -32), (-12, -55, 89, -62, -47, 1, -16, -7, -89, -92), (-66, 98, -72, 59, 48, 56, -81, -89, -2, -24), (46, -49, 41, 78, 5, 64, -49, 84, -3, -29), (76, 36, 68, -44, -76, -42, -73, 53, 75, -98), (-78, 72, -65, 70, 25, -7, -32, 7, -35, 59), (39, 93, 60, -49, -84, 16, 4, -35, -88, 66), (-84, -18, -82, 52, 3, 36, -30, 63, -68, 54), (50, -39, 92, -56, 7, -45, -51, -15, 31, -91), (34, 57, -99, -1, -83, -18, -82, -29, -10, -72), (96, 96, 40, 25, 83, -18, -56, 51, -69, -88), (32, 56, 82, 9, -34, -51, -22, -39, 64, 59), (76, 30, 13, -87, -79, 14, -16, -24, -30, 96), (-81, -73, -4, 38, 13, 40, -10, -8, 53, -73), (85, 27, -34, 84, 39, 88, -79, -31, 31, 43), (-23, -29, 94, -47, 28, -94, 71, 80, 10, -3), (-68, 71, 13, -75, 9, 50, 40, -85, 64, 21), (-5, 74, 93, -93, 1, -52, -4, -2, 59, 78), (38, 28, 51, 31, 9, 89, 10, -60, -32, 64), (45, -2, -76, 25, -50, 58, -2, -74, 76, -67), (-64, -41, -94, 46, -16, 35, 81, -77, -68, -71), (-59, -9, 40, 6, -4, -2, 50, -34, 9, 76), (64, -97, 36, -36, -78, 20, -69, -25, -35, -12), (42, -95, -87, 51, -77, -75, -65, 34, -42, -78), (75, -98, -87, -86, -43, 29, 75, -98, -80, -62), (55, 58, -72, -55, 90, 27, 91, 78, -67, 66), (50, -49, -97, 37, 17, -98, 52, 10, -25, 45), (-65, -42, 14, -9, -51, -72, 87, 35, -15, 53), (-8, -21, -17, -73, -22, -87, 51, -22, -25, 40), (32, 45, 68, -78, -24, 42, 26, -23, 67, 36), (80, 11, -50, -88, -30, -76, -45, -40, -11, 28), (-53, 43, -22, -76, -84, 98, -73, -53, -29, 16), (-93, -8, 5, 34, 69, -67, -36, 18, -43, -88), (-18, 83, -62, 99, 6, -88, 5, 39, 12, -78), (-51, -20, -56, -67, -15, -84, 69, 85, 80, -52), (11, -69, -65, 28, -17, 20, 1, 7, -72, -8), (26, -37, -6, 16, 85, -92, 0, -39, 81, 57), (64, -74, 67, 13, -2, 83, 21, 24, 52, 67), (-73, -74, 92, 20, 62, -16, -51, 54, -41, -15), (-49, 39, 96, 44, 33, 21, -42, -21, -82, -43), (50, -24, -91, -29, 60, -96, 60, -62, 1, 73), (88, 71, -60, -3, -14, 28, 18, 85, 90, 30), (15, 3, -6, 69, -34, 46, 55, -99, 78, 15), (13, 54, -20, -47, -48, -20, -26, 66, -4, 37), (-47, -52, 50, 22, 13, -81, 42, -25, -39, -32), (30, -44, 14, 67, -64, -84, 82, -3, 97, 1), (-4, -66, -19, -87, -8, 46, -48, -81, -16, 74), (-40, 0, -85, -88, 22, 28, 4, -62, -89, 36), (39, -33, -62, -84, 21, -89, -35, -70, -44, 14), (-63, 97, -87, -64, 85, -67, 13, 76, -20, -66), (-97, 44, -26, 57, 98, 50, -50, -56, 88, 9), (82, 18, -31, 33, -90, -92, -35, -89, -81, -66), (84, 19, 30, -77, -25, 79, 59, -16, 69, -65), (4, 42, 42, 23, 57, 60, -39, 1, -21, -47), (44, 19, -53, -55, 62, -92, 16, -84, -23, 24), (-13, 15, -18, 41, -50, -39, 29, -33, -5, -69), (43, 10, -17, 69, -77, 38, 79, 88, -8, -44), (-12, 62, 28, -58, 19, -65, 41, 87, -46, -98), (40, -91, -13, 86, 17, 26, 37, 78, -57, -46), (-60, -32, 15, -96, 16, 53, -5, 44, -57, -78), (37, -92, 59, -83, 66, 83, 57, -20, 92, 33), (66, -63, 40, 76, 83, 73, 39, 10, -83, 65), (-45, 67, 13, -51, 40, -41, -87, -73, 28, -19), (-94, -48, -50, -58, -49, 21, 71, 93, -84, 26), (93, 13, 78, 57, 81, -75, -65, -82, -76, -60), (-80, -38, 96, -36, 92, -94, -96, -9, -67, -72), (-56, -78, 11, 16, 91, 61, -2, -24, -4, -11), (88, -55, 2, -37, -24, -30, 38, -48, 47, 21), (18, 95, 34, 69, 49, -35, 77, 23, -68, 34), (49, -69, -79, 0, -97, -19, -79, 22, 13, -39), (-22, 34, -54, 62, -40, 96, -62, -10, -42, 83), (-60, 81, -88, 47, -99, 72, -45, 27, -61, 86), (-2, 63, -88, -76, -94, 21, 14, 24, 76, 65), (33, -22, -75, -34, -59, 6, -81, 1, -71, 32), (-58, -7, -12, 15, -28, -87, -59, 26, -39, -37), (95, 77, 92, -36, 41, 21, -89, 69, -79, -43), (-28, 20, -43, 29, 65, -34, 63, -93, -1, -10), (65, 18, 19, 83, 69, -26, -16, -6, 86, 22), (-54, 86, -53, 14, 92, -4, -73, 2, -79, -85), (-14, -86, 21, -60, 82, -96, 42, -97, -49, 40), (9, 19, 70, 61, 74, -12, 88, 92, 6, 48), (-51, -96, 91, -66, -75, 62, -53, 29, 18, -37), (-51, -88, -28, -8, 2, 60, -61, -86, 48, -96), (-12, 38, 77, -99, -21, -18, 75, 67, -74, 84), (-27, 81, -63, -94, 39, 50, -22, 40, 81, -58), (70, -45, 11, 23, 14, -6, 92, -37, 86, -46), (46, -89, 35, -47, 96, 81, 89, -12, -81, -23), (30, 89, -49, 87, 6, 92, -75, 69, -81, 14), (92, -97, -41, -31, 62, -57, -9, -52, 98, 59), (-77, 35, 39, -61, 92, -24, -2, 83, 44, 7), (30, -71, -46, 70, -59, 79, 89, -31, 75, -3), (-67, -8, 53, 48, 86, 28, -39, 12, -67, 36), (-12, 73, 32, 40, 65, 40, -98, 98, 76, -88), (-32, -98, -15, 40, 99, 23, -83, 44, -43, -48), (-54, 73, -63, 96, -39, -47, -9, -39, -1, -92), (25, -83, -5, -31, 11, 84, -86, -60, 83, -26), (-69, 71, 2, -42, -54, 5, 66, 70, -25, -71), (2, -97, -17, -10, 43, -79, -42, -81, -87, 20), (-82, 36, 85, 52, 3, -11, 17, -2, 83, 97), (44, -40, 70, -98, -62, -65, -16, 50, 76, 20), (-22, 4, 45, -29, -67, -54, 14, 57, 42, 41), (81, 22, 73, 33, 27, -76, 39, 99, -48, 55), (-93, -20, -59, -44, -72, -7, 67, -77, -57, -83), (-17, -31, -80, 94, -83, 37, 14, 32, -14, 54), (11, -55, -6, -16, 60, 28, -52, -43, -80, -55), (31, -22, 3, -26, 82, 36, 50, -37, -42, 49), (83, -4, -38, 64, 25, 11, -55, 67, 3, 47), (25, -33, 40, -10, -67, -19, 68, -80, -92, -67), (91, -68, 16, 51, -86, -38, -51, -16, -10, -24), (68, 28, -2, -47, 27, 18, 74, -75, -39, -62), (51, -27, -18, 59, 93, -94, 29, 96, 22, 9), (44, 53, 59, 98, -99, -93, -95, -52, -85, 22), (-35, 42, 92, 75, 19, 47, -78, 15, -11, 88), (85, -15, -45, 57, 60, -62, 62, -9, -63, -22), (-60, -46, 65, 26, -79, -23, -65, 41, 9, 21), (-17, 96, 81, 33, -72, -96, -12, 10, 14, -62), (-79, -2, 89, 43, 42, -58, -2, -28, -55, 96), (69, 27, -29, 46, -57, 56, 38, 1, 15, -86), (21, -96, -71, -84, -64, -82, -99, 92, 91, -12), (-87, -89, -51, -72, 86, -2, 42, -16, -23, 95), (24, 9, -73, 66, 99, 42, 60, 5, -29, 49), (-56, 86, 98, 52, -93, -80, 85, -37, -20, -71), (42, -46, -95, -31, 98, 13, 37, 90, -11, -72), (-6, -38, -23, 15, -9, 69, 26, -73, -17, -89), (60, -8, -94, 65, 98, 78, -44, -78, -28, 79), (-46, -59, 42, 10, -97, 8, -10, -51, -57, 29), (-21, -84, 32, 58, -98, 34, -32, -57, 18, -14), (-35, -65, 14, 46, 85, -70, -85, -60, 56, -27), (-58, 78, -77, 22, -13, 14, 65, -52, -93, 77), (98, 33, 70, 69, -46, -56, -77, 58, 95, 7), (44, -99, -36, 31, 51, 1, -43, 89, -22, -8), (-73, -94, -81, 8, -23, 59, 31, -55, 55, 76), (29, 20, 65, -80, -55, -42, -49, -29, -38, 60), (55, 21, 29, -55, 94, -96, -97, -66, 69, -15), (-35, -56, 77, 97, -91, -64, 22, -75, -96, -73), (-60, -54, -80, -22, -91, -54, -19, 15, -74, 47), (-97, -15, -7, -88, -12, 36, 47, -75, -50, -41), (39, 41, -86, -91, 56, -30, 33, 57, 0, 99), (71, 1, -53, -65, -80, 93, 24, 4, 93, 99), (4, -56, 35, -9, -77, -46, 31, -16, -37, 99), (73, -18, 11, -86, 10, 16, 33, 9, 42, 18), (18, -37, 31, 83, 66, 25, 72, -54, 80, 70), (-96, 79, -86, 63, 24, -36, 82, 94, 21, -25), (67, -19, -4, 88, 89, -61, 35, 99, 9, 97), (-63, -82, 50, -35, -83, 79, -8, 2, 36, 48), (19, -69, 10, -25, 63, -91, -27, 98, -92, -30), (-40, -32, 49, -46, 15, -63, -25, -57, 8, 42), (40, -19, 92, 73, -76, -18, -94, 16, -48, 82), (-69, -65, -77, -26, -4, -2, -69, -27, 34, -47), (70, 79, 68, -85, -2, -57, 61, -64, 87, 81), (-66, 6, -62, 50, 57, -92, -81, 21, 88, -27), (62, 89, -12, 44, 35, -81, 80, -27, 25, -42), (46, -32, -50, -64, 25, 34, 81, -55, -10, -37), (55, -73, -56, 15, -34, -74, -2, 68, -70, 81), (-69, -8, 4, -79, 73, 48, 41, 99, 76, 81), (40, 48, 77, 16, -5, -54, -81, 56, 2, -31), (-68, 90, -98, -11, 85, 9, -94, -31, 24, 7), (-32, -65, 89, -31, 47, -57, -69, 37, -8, -40), (-78, -30, -34, -74, 3, -27, -39, -6, 23, 17), (-24, 0, -83, 18, 77, -63, 10, 94, -51, -3), (2, 56, -34, 74, 14, -30, 41, -63, -66, 88), (10, -28, -55, 82, -84, -75, -18, 36, 81, -68), (12, 2, -35, -22, 61, -92, 61, 90, 72, -9), (-80, 11, -9, -6, -23, 80, -14, 80, -58, -31), (-5, -96, -39, -4, 3, 1, 47, 56, -4, 53), (-68, -18, -99, 2, -51, -47, -37, 8, -77, 85), (-99, 14, -98, 15, -17, 61, 79, -84, 58, 96), (36, -10, 99, 48, 23, 74, 92, 1, 71, -50), (-21, 42, 14, -13, -13, -8, -17, -88, -50, -95), (-72, -32, 81, 37, 40, 95, 49, 12, -38, -38), (50, 92, 1, -71, 59, 88, 32, -54, 97, 5), (-47, 40, -11, -51, 25, -32, -22, 77, -98, 37), (-61, 54, -24, -26, 0, 11, -3, 57, -71, -58), (76, -64, 23, -2, -93, -87, 82, 93, -66, 25), (-21, -24, 24, 69, 71, -87, -60, 2, 24, -55), (13, -26, -57, -20, 66, -16, 31, 25, 15, -24), (80, 0, 43, -19, -87, 97, 44, -73, -2, 36), (87, 35, 18, -9, -63, 19, 16, -11, 74, 60), (50, -1, -53, 51, -99, -25, 89, -75, -85, -10), (49, -7, -15, 60, 35, 27, -62, 47, -32, -22), (-24, -87, -12, 71, 44, -96, 22, -97, 49, 62), (78, -9, 48, 76, 72, 84, 26, 78, 20, -11), (-8, -68, 69, -4, 13, 83, 51, -82, -7, 82), (-33, 62, -25, -53, -19, -81, 2, 56, 38, -5), (-69, -63, 94, -29, 48, -59, 32, 29, -64, 99), (12, -40, -85, 19, -96, -32, -42, -40, 26, 18), (-71, 59, -69, 7, -25, 45, -4, 52, 32, 24), (50, -10, 72, -71, 45, 13, 79, 6, -23, 21), (62, 43, -29, -4, -59, 84, 48, -20, 8, -66), (98, 88, 55, 1, 53, -93, 29, 78, 79, 79), (81, 6, 76, -40, 96, -28, -67, -24, 41, -8), (88, -27, -88, 34, -28, 56, -81, 62, -3, 1), (-89, -84, -3, -30, -32, 82, 49, 69, -57, -51), (-82, -95, -34, 21, -72, -86, -79, -99, -41, 25), (48, 67, 14, -8, -63, 15, 37, 73, -77, 30), (-66, -73, -60, 83, -83, 8, 12, -27, 20, 57), (96, 23, -34, -52, 0, 72, 75, 78, -54, -62), (-46, 89, -22, 68, 85, 40, -88, -51, -54, 9), (17, 86, -10, -41, -99, -61, 88, -51, -53, 31), (-12, 25, 55, 31, 3, 88, 61, 97, 51, -2), (51, -18, -63, 85, 51, -71, 35, -10, -74, 11), (-81, 94, -54, 55, 36, 66, 30, -16, -13, 26), (6, 84, 18, 53, -31, 35, -39, 71, -61, -34), (-21, -47, -42, 32, -80, 59, -85, 20, 11, -84), (-33, -9, -69, -48, -86, 43, 6, -42, -49, 44), (35, 70, 78, -85, 58, 54, 71, 33, -76, -24), (-93, 92, 23, 44, -40, -50, 84, 7, 13, -47), (74, 48, -34, -35, -86, 84, -90, 44, -23, 43), (1, 9, 75, -14, 31, -86, 0, 5, -60, -35), (-99, -7, 12, -76, -27, -57, -28, -56, -85, -19), (-58, -31, -91, -41, 14, -33, 14, -29, -35, -35), (-84, 29, -45, 16, -50, 99, 14, 21, -84, -44))
