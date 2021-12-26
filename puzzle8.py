with open("input8.txt", "r") as file:
    data = file.read().splitlines()
# data = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe \n" \
#        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc \n" \
#        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg \n" \
#        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb \n" \
#        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea \n" \
#        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb \n" \
#        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\n" \
#        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\n" \
#        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\n" \
#        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce\n"
# data = data.splitlines()

output = 0
for line in data:
    line = line.split(" ")
    for code in line[11:]:
        if len(code) in [2, 3, 4, 7]:
            output += 1
print(output)

line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
line = line.split(" ")
digits = list(range(0, 10))
digit_dict = {}
for d in digits:
    digit_dict[d] = "abcdefg"
# print(digit_dict)

a = "abcdefg"
b = "abcdefg"
c = "abcdefg"
d = "abcdefg"
e = "abcdefg"
f = "abcdefg"
g = "abcdefg"
base = "abcdefg"
variables = [a, b, c, d, e, f, g]
segment_dict = {"a": base, "b": base, "c": base, "d": base, "e": base, "f": base, "g": base}
for code in line[0:10]:
    # print(code)
    # a = segment_dict["a"]
    # b = segment_dict["b"]
    # c = segment_dict["c"]
    # d = segment_dict["d"]
    # e = segment_dict["e"]
    # f = segment_dict["f"]
    # g = segment_dict["g"]
    if len(code) == 2:
        digit_dict[1] = code
        for letter in base:
            if letter not in code:
                segment_dict["c"] = segment_dict["c"].replace(letter, "")
                segment_dict["f"] = segment_dict["f"].replace(letter, "")
            # else:
            #     a = a.replace(letter, "")
            #     b = b.replace(letter, "")
            #     d = d.replace(letter, "")
            #     e = e.replace(letter, "")
            #     g = g.replace(letter, "")
    if len(code) == 4:
        digit_dict[4] = code
        for letter in base:
            if letter not in code:
                segment_dict["b"] = segment_dict["b"].replace(letter, "")
                segment_dict["c"] = segment_dict["c"].replace(letter, "")
                segment_dict["d"] = segment_dict["d"].replace(letter, "")
                segment_dict["f"] = segment_dict["f"].replace(letter, "")
    if len(code) == 3:
        digit_dict[7] = code
        for letter in base:
            if letter not in code:
                segment_dict["a"] = segment_dict["a"].replace(letter, "")
                segment_dict["c"] = segment_dict["c"].replace(letter, "")
                segment_dict["f"] = segment_dict["f"].replace(letter, "")

# print(segment_dict)
for key, segment in segment_dict.items():
    if len(segment) == 1:
        for k, s in segment_dict.items():
            if len(s) == 1:
                continue
            segment_dict[k] = s.replace(segment, "")
    if len(segment) == 2:
        # print("segment=" + segment)
        for k, s in segment_dict.items():
            if len(s) == 2:
                continue
            segment_dict[k] = s.replace(segment[0], "").replace(segment[1], "")

            # print("s=" + s)

for key, segment in segment_dict.items():
    if len(segment) == 1:
        for k, s in segment_dict.items():
            if len(s) == 1:
                continue
            segment_dict[k] = s.replace(segment, "")
    if len(segment) == 2:
        # print("segment=" + segment)
        for k, s in segment_dict.items():
            if len(s) == 2:
                continue
            segment_dict[k] = s.replace(segment[0], "").replace(segment[1], "")

            # print("s=" + s)
print(segment_dict)
five = segment_dict["a"]+segment_dict["b"]+segment_dict["d"]+segment_dict["f"]+segment_dict["g"]
print("".join(set(five)))
# for v in variables:
#     print(v)
#     if len(v) == 1:
#         for letter in v:
#             for vari in variables:
#                 vari = vari.replace(letter, "")
#     if len(v) == 2:
#         for letter in v:
#             for vari in variables:
#                 vari = vari.replace(letter, "")
# if len(code) == 7:
#     digit_dict[8] = code
#     for letter in base:
#         if letter not in code:
#
#             c.replace(letter, "")
#             f.replace(letter, "")
# print(segment_dict)
# print("a = " + a + ", b = " + b + ", c = " + c + ", d = " + d + ", e = " + e + ", f = " + f + ", g = " + g)


# for digit in line[11:]:
#     print(digit)
