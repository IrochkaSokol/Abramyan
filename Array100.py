def Array100(s):
  for i in s:
      k = 0
      for j in s:
          if i == j:
              k += 1
      K.append(k)
  h = 0;
  for i in range(n):
      if K[i] == 2:
          del s[i - h]
          h += 1
  return s
