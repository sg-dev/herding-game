# Plan

## Implementation

Contents
--------

 * One-shot 2-Player
 	* Overview
 	* Command-line arguments
 	* Function simulating bot(s)
 	* Model
 	* Pages
 	* Time-planning
 * One-shot Multiplayer
 	* Overview
 	* Command-line arguments
 	* Function simulating bot(s)
 	* Model
 	* Pages
 	* Time-planning
 * Repeated Multiplayer
 	* Overview
 	* Command-line arguments
 	* Function simulating bot(s)
 	* Model
 	* Pages
 	* Time-planning


One-shot 2-Player
-----------------

#### Overview
We build a Prisoner's Dilemma game with the possibility of giving to the player a fraction of the cooperators payoff if they cooperated and a bonus (with some probability) regardless of their decision. Hereby, the players are a human player and 1 hardcoded bot as specified below.

#### Command-line arguments
* d: Bot decision
* Î±: Fraction of total payoff redistributed to cooperators
* Î²: Bonus given to player w.p. p if cooperator and w.p. q if defector

#### Function simulating bot(s)
When assigning payoffs, check whether player has chosen C, D and toss a coin u.a.r. (w.p. 1/2) to decide d = C, D for the bot.

#### Model
Usual PD model with addition of (Î±, Î²) options.

#### Pages
* Let the player choose its action as usual.
* Implement bot.
* Record results.

#### Time-planning
4 hours 


One-shot Multiplayer
--------------------

#### Overview
We build a Prisoner's Dilemma game with the possibility of giving to the player a fraction of the cooperators payoff if they cooperated and a bonus (with some probability) regardless of their decision. Hereby, the players are a human player and multiple hardcoded bot as specified below.

#### Command-line arguments
* f: Fraction of bot cooperators
* Î±: Fraction of total payoff redistributed to cooperators
* Î²: Bonus given to player w.p. p if cooperator and w.p. q if defector

#### Function simulating bot(s)
When assigning payoffs, check whether player has chosen C, D and compute payoff according to fraction of bot cooperators f.

#### Model
Usual PD model with addition of (Î±, Î²) options.

#### Pages
* Let the player choose its action as usual.
* Implement bot.
* Record results.

#### Time-planning
2 hours


Repeated Multiplayer
--------------------

#### Command-line arguments
* f[]: Fraction of cooperators (over rounds)
* Î±[]: Fraction of total payoff redistributed to cooperators (over rounds)
* Î²[]: Bonus given to player w.p. p if cooperator and w.p. q if defector (over rounds)

#### Function simulating bot(s)
When assigning payoffs, check round t and whether player has chosen C, D and compute payoff according to fraction of bot cooperators at that round f[t].

#### Model
Usual IPD model with addition of (Î±, Î²) options.

#### Pages
* Let the player choose its action as usual.
* Implement bot.
* Record results.

#### Time-planning
4 hours

## Tutorials
Please read the following the two tutorials for a deeper understanding of the repository:
* `PD_tutorial.md` is especially useful if you would like to see a walked-through example of the One-Shot 2-player/Multiplayer Prisoner's Dilemma with (Î±, Î²) options.
* `IPD_tutorial.md` is especially useful if you would like to see a walked-through example of the Repeated Multiplayer Prisoner's Dilemma with (Î±, Î²) options.

#### Time-planning
2 hours

## Ready-to-use repository [TODO]
You could clone the finished and ready to use repository we have built

```bash
git clone 
```

#### Drag & drop [TODO]
* Once the repository is cloned, navigate to the folder `otree/iterated_prisoners_dilemma` and copy it, in its entirety, inside the `<PATH>/oTree` folder where oTree has been installed previously (refer to the **Getting Started** section in `abm-tutorial.md`). 
* Replace the `settings.py` script present in `<PATH>/oTree` with the one in `./abm-course-otree/otree`. Please be aware that the `settings.py` in `./abm-course-otree/otree` does not include the games you have implemented but only the ones we implemented. Thus, please add the games you have created to settings as explained in the tutorial https://otree.readthedocs.io/en/latest/tutorial/part2.html.

#### Running [TODO]
Assuming to be inside the `<PATH>/oTree` directory, for playing yourself at the browser run the command `otree devserver` in the Terminal window, and go to `http://localhost:8000/` in a browser of your choice.

## Deployment [TODO]

The deployed version of this repository may be found at .

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [oTree](https://www.otree.org/) - The game theory framework built on top of Django
* [Highcharts](https://www.highcharts.com/) - The charts library used within JS template scripts

## Authors

* [**Matteo Russo**]()

* [**Giacomo Vaccario** ](https://www.sg.ethz.ch/team/people/gvaccario/)

* [**Luca Verginer** ](https://www.sg.ethz.ch/team/people/lverginer/)
