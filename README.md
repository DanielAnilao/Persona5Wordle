# Persona 5 Royal Wordle

##### It's wordle, but it uses Personas from Persona 5 Royal

## Introduction

## Purpose

This SRS will go over a Persona 5 Royal themed Wordle, based in a web application. It will explain how this "wordle" works, what are the rules, and any other extra things the web app will do.

## Scope

This document contains a complete description of the functionality
of the Persona 5 Royal Wordle project. It consists of use cases, functional requirements and nonfunctional requirements,
which, taken together form a complete description of the web application.

## System Overview

The functionality of the project shall be within a web application with the support of a database to gather and store information. Users will give a Persona from the game and then will be told what matches and does match with the "Persona of the Day."

## References

Persona Fusion Calculator: https://chinhodado.github.io/persona5_calculator/indexRoyal.html#/list

This website has information on all the Personas.

## Definitions

Persona:

1. A Japanese Role Playing Video Game series made by Atlus.
2. A "creature" that resides in the soul/heart of a being. Controlled by many means. In Persona 5, they are called on by tearing off a mask made by the spirit of rebellion within a being.

"Persona of the Day"

## Use Cases

| Name                   | UC - 1: Import information from Database                                                                                                                                                        |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Summary                | Bring information from Persona database to web app.                                                                                                                                             |
| Rational               | The database will contain information about every Persona from Persona 5 Royal. It will be necessary to import the data from this database so that the comparisons can be made.                 |
| Users                  | All Users                                                                                                                                                                                       |
| Preconditions          | Functioning Database with information about all the Personas.                                                                                                                                   |
| Basic Course of Events | <ul><li>1. When starting the web app, all the information from the database should be added immediately. </li><li>2. When typing a valid Persona, the stats of the Persona should be displayed. |
| Postconditions         | Information should be accessable in the Web App.                                                                                                                                                |

| Name                   | UC - 2: Comparing Information                                                                                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Summary                | Compare information from the user given Persona to the "Persona of the Day."                                                                                                                           |
| Rational               | The purpose of Wordles is to compare your word to the "word of the day" so we're taking that same logic but with the stats from Persona.                                                               |
| Users                  | All Users                                                                                                                                                                                              |
| Preconditions          | Functioning Database is connected with the Web App and can compare live infomation to the infomation in the database.                                                                                  |
| Basic Course of Events | <ul><li>1. When the user enters in a valid Persona, it will check the stats of the entered Persona. </li><li>2. The web app should check the stats of the entered Persona and the "Persona of the Day" |
| Postconditions         | <ul><li>The application will be able to determine if an entered Persona is correct or not.                                                                                                             |

| Name                   | UC - 3: Entered Personas                                                                                                                                                   |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Summary                | Displays what Persona(s) the user already entered.                                                                                                                         |
| Rational               | This keeps track of which Personas the user has entered for the game. Any wordle like game keeps track of previously entered phrases to help the user.                     |
| Users                  | All Users                                                                                                                                                                  |
| Preconditions          | User entered in a Persona                                                                                                                                                  |
| Basic Course of Events | <ul><li>1. After the user enters in a Persona it should continue to be displayed for reference.                                                                            |
| Postconditions         | Any incorrect Personas entered in by the user should be displayed and show simularities and differences. If the user entered the correct Persona they should be told that. |

## Functional Requirements

| Name         | FR - 1: Persona Preview                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| Summary      | As the user types in a Persona's name, a list of possible Personas will show up.                                                      |
| Rational     | There's more than 100 Personas. Entering something close to the name would help a user who isn't using an outside source.             |
| Requirements | <ul><li>1. Reading information from Persona Database. </li><li>2. App reads in currently typed in letters and returns possible names. |
| References   | UC-1 Import Information from Database                                                                                                 |

| Name         | FR-: 2 Cross Examination                                                                                                                                |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Summary      | Checks each stat of the entered Persona and compares them with the given "Persona of the Day"'s stats.                                                  |
| Rational     | A comparison is necessary as it's the main mechanic of the game.                                                                                        |
| Requirements | Each time the user enters in a valid Persona, the application will compare each stat. The stats being Arcana, Inherit Type, and any element affinities. |
| References   | UC- 2 Comparing Information                                                                                                                             |

| Name         | FR- 3: List of Personas                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Summary      | Below the display of stats, an entered Persona should be added.                                                                                                                          |
| Rational     | All wordles save entered in phrases to cross reference.                                                                                                                                  |
| Requirements | <ui><li> 1. After entering a valid Persona it will be saved under a display showing the stats of the Persona. </li><li> 2. All of the stats will be displayed alongside entered Persona. |
| References   | UC- 3 Entered Persona                                                                                                                                                                    |

| Name         | FR- 3: Incorrect Personas                                                                                                                         |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Summary      | If stats don't match, Persona is deemed incorrect, but is saved to the list.                                                                      |
| Rational     | Tells user they are wrong but will get hints to what stats are right and wrong.                                                                   |
| Requirements | <ui><li> 1. After getting displayed any stats that are incorrect will be a red color </li><li> 2. While any matching stats will be a green color. |
| References   | UC- 2 Comparing Information UC- 3 Entered Persona                                                                                                 |

## Nonfunctional Requirements

| Name         | NF-1: |
| ------------ | ----- |
| Summary      |       |
| Rational     |       |
| Requirements |       |
| References   |       |
