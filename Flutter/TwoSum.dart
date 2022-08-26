void main() {
  var listofNums = [1, 2, 3, 4];
  int target = 6;
  for (var a = 0; a < listofNums.length; a++) {
    for (var b = a + 1; b < listofNums.length; b++) {
      int sum = listofNums[a] + listofNums[b];
      if (sum == target) {
        print("${listofNums[a]},${listofNums[b]}");
      }
    }
  }
}
