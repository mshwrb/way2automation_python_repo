*** Variables ***
${Name}=    Corry
${Num1}=    10
${Num2}=    20
*** Test Cases ***
If Block Test Case Example
     IF    "${Name}" == "Keshav"
           log to console    Name is Keshav
     ELSE
           log to console    Name is not Keshav
     END

Else if Block Test Case Example
     IF    "${Name}" == "Keshav"
           log to console    Name is Keshav
     ELSE IF    "${Name}" == "Corry"
           log to console    Name is Corry
     ELSE
             log to console    Name is does not match
     END

Number Comparision
     IF  ${Num1} == ${Num2}
         log to console    ${Num1} is equal to ${NUm2}
     ELSE IF    ${Num1} < ${Num2}
         log to console    ${Num1} is less ${NUm2}
     END

Multiple Conditions
     IF    ${Num1} < ${Num2} and ${Num1} < 9
           log to console    ${Num1} is less than ${NUm2} and less than 9
     ELSE IF    ${Num1} < ${Num2} or ${Num1} < 9
           log to console    ${Num1} is less than ${NUm2} or less than 9
     END
