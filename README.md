# Custom Media Catalogue with Advanced Error Handling

A robust, object-oriented Python application designed to manage, filter, and display various media components (`Movie` and `TVSeries`) while demonstrating defensive programming through custom exception architectures.

## 🚀 Key Features

- **Strict Type Separation**: Utilizes explicit `type()` evaluations over standard `isinstance()` checks to distinctly filter and categorize base classes from inherited child classes.
- **Context-Aware Exceptions**: Implements a custom `MediaError` class that encapsulates the exact runtime object causing an anomaly, streamlining root-cause analysis during debugging.
- **Dynamic Catalogue Formatting**: Features an intelligent `__str__` layout generator that partitions, enumerates, and presents media assets dynamically by type.

## 🛠️ Architecture Overview

- **`Movie` (Base Class)**: Validates core primitives (Title, Year, Director, Duration) ensuring string cleanliness and logical boundaries (e.g., cinema-epoch year restrictions).
- **`TVSeries` (Derived Class)**: Extends `Movie` to inherit metadata while adding fields for structural parameters like seasons and episode footprints.
- **`MediaCatalogue` (Controller)**: Acts as the collection state manager, enforcing type safety on intake and exposing filtered tracking methods (`get_movies`, `get_tv_series`).

## 💻 Sample Output

```text
Media Catalogue (4 items):

=== MOVIES ===
1. The Matrix (1999) - 136 min, The Wachowskis
2. Inception (2010) - 148 min, Christopher Nolan

=== TV SERIES ===
1. Scrubs (2001) - 9 seasons, 182 episodes, 24 min avg, Bill Lawrence
2. Breaking Bad (2008) - 5 seasons, 62 episodes, 47 min avg, Vince Gilligan
```
