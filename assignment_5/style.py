
foo  = long_function_name(var_one, var_two,
             var_three, var_four)


 def long_function_name(
             var_one, var_two, var_three,
                 var_four):
         print(var_one)

""" The foo variable needs the variables in the function aligned with opening delimiter:
"""
foo  = long_function_name(var_one, var_two,
                          var_three, var_four)

""" and def neds to have the variables aligned and then the call to print back in:
"""
def long_function_name(
        var_one, var_two,
        var_three, var_four): 
    print(var_one)

# operators: prefix or postfix?
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

""" operators should be before for readablity """
income = (gross_wages
        + taxable_interest
        + (dividents - qualified_dividends)
        - ira_deduction
        -student_loan_interest)

def top_level_func():
        print("important processing going on here")

        def second_func():


                print("another gravely important function")
""" remove space between def second and call to print """ 

def top_level_func():
        print("important processing going on here")

        def second_func():
                print("another gravely important function")

def topLevelFunc():
        print("important processing going on here")
            mixedCaseVariables = True

""" I think the issue with above is that function and variable shouldn't be mixedCase unless the whole script is that way""" 
def top_level_func():
        print("important processing going on here")
            mixed_case_variables = True
