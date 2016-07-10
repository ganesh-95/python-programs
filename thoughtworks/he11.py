i = 0
j = n-1
while(i < j){
   if      (a[i] + a[j] == target) return (i, j);
   else if (a[i] + a[j] <  target) i += 1;
   else if (a[i] + a[j] >  target) j -= 1;
}
return NOT_FOUND;
