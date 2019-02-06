#!/usr/bin/env python3

#try-except-finally:    finally is executed EVERY TIME (no matter is there an axception or not.
#try-except-else:       else is executed ONLY WHEN NO EXCEPTION (ELSE RELATES TO EXCEPT).

#finally ie executed everytime, else-only without exception.

#try    except  finally (every time)
#True   False   yes
#False  True    yes

#try    except  else (when no exeption)
#True   False   yes
#False  True    no    

try:
    print(8/0)
except ZeroDivisionError:
    print("2. except")
finally:
    print('3.finall')
print('*****************************')
try:
    print(8/0)
except ZeroDivisionError:
    print("2. except")
else:
    print('3. else')
