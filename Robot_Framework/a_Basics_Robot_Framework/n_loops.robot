*** Variables ***
@{city}=    Delhi    Mumbai    Goa
*** Test Cases ***
Looping 1
    # This will print from 0 to 4 (1 less than value given in range)
    FOR    ${i}    IN RANGE    5
         log to console    ${i}
    END

Looping 2
    # 2 here is incrementer
    FOR   ${i}  IN RANGE    1    10    2
         log to console    ${i}
    END

Looping 3
    # -2 here is decrementer
    FOR   ${i}  IN RANGE    10    1    -2
         log to console    ${i}
    END

Looping 4
    # 2 here is incrementer
    FOR   ${i}  IN RANGE    1    10    2
         log to console    ${i}
         exit for loop if    ${i} == 5
    END

Looping 5
    # 2 here is incrementer
    FOR   ${i}    IN  @{city}
         log to console    ${i}
         exit for loop if    '${i}' == 'Mumbai'
    END