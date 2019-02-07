#!/usr/bin/env python3

#try-except-finally:    finally is executed EVERY TIME (no matter is there an axception or not).
#try-except-else:       else (RELATES TO EXCEPT) is executed ONLY WHEN NO EXCEPTION.
#finally is executed everytime, else-only without exception.

#try    except  finally
#True   False   yes    (every time)
#False  True    yes    (every time)

#try    except  else
#True   False   yes  (only when no exeption)
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
