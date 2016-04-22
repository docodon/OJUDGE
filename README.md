# OJUDGE
It is an implementation of online judge (a platform where a programming contest can take place) .
Here , one can host a one contest at a time .

MADE using Django(1.7)/Python , HTML/CSS/Java-script and Ideone's api.

Functionalities : 

    1) Admin - Can add problems , test-cases and set contest time . 
    2) One can register for a contest (3-members in a team are must) , login , logout of the platform .   
    3) During contest one can submit Solutions for the problems displayed on the contest link and view the rankings table .


Structure is divided in three apps :


1)  REGISTER :
    It contains the home page and candidates can register over here .
    
2)  PSET :
    The Admin side and admin can add problems , testcases and set time for the contest .
   
3)  CONTEST :
    When contest is real-time.Various functionality in this app are : Login page for teams , ranking-table , problems-page 
    ,problem description for every problem  , source code submission and generating result of the submission .


Models/Tables : 

 1) PSET (APP_NAME): 
  
    - (TABLE NAME)=problem - (ATTRIBUTES)=[ pcode , pdesc ] -> (ATT. DESC.)=[ problem_code , problem_desc.]
    - testcases - [ pcode , inp , out ] -> [ problem_code , input_file , output_file ]
    - timer     - [ stime , etime ]   -> [ start_time_of_contest , end_time_of_contest ]
 
 2) REGISTER : 
    - team - [ user , name , member1 , member2 , member3 , password ] -> [ team_handle(for login) , team_handle(for login) , name_member1 , name_member2 , name_member3 , password_for_login ]
 
 3) CONTEST :
    - teamr - [ tname , acs , time ] -> [ team_handle , number_of_ACcepted_solutions , total_time_for_all_ACs ]
    - accepted - [ pcode , tname , code ] -> [ problem_code , team_name , source_code_submitted ]    

PLEASE SEE : 

SINCE IDEONE API is used in this project : 
One needs to have ideone username and ideone api password . ( Its free , once you having account at :  http://ideone.com/)

And PUT YOUR CREDENTIALS AT /contest/views.py line 85 and 86 .
