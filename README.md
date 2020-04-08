OSD-Study
===========

### Hardware: button types

1. Mouse wheel
2. D-pad
3. Joystick
4. Spinwheel on DSLR

### UI/Design

1. List-like
2. Wheel-like 

### Experiment Design

1. **RT** focused 
2. **ACC** focused

## To-Do list

- [ ] Practice Trials ----  
- [ ] Experiment Trials ----  
    - [ ] baseline
- [ ] Save files & Thanks ----  

### My memo

```Python
def function_A():
    # Translate response key to meaningful tag
    if response == 1:
        tag = 'Up'
    elif response == 2:
        tag = 'Down'
def function_B():
    # Determine how the program should react
    if tag == 'Up':
        action = NextPage
    elif tag == 'Down':
        action = PreviousPage
def function_C():
    # Trim off unwanted data points
    if response == PreviousResponse:
        dataCleaning = Trim_Off
    elif response != PreviousResponse:
        dataCleaning = Send_to_file
```

```Python
    item, expStatus = response_key(buttons, times, item, nStimulus, expStatus) 
    # the function 'response_key' export 2 variables.
    # in this way, I can use a function to affect outside world(main program)
```
