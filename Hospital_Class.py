{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "id": "Uo2gcRjakck6"
      },
      "outputs": [],
      "source": [
        "class Hospital:\n",
        "  def __init__(self, name, list_of_departments):\n",
        "    self.name = name\n",
        "    self.list_of_departments = list_of_departments\n",
        "\n",
        "  def show_departments(self):\n",
        "    print(\"These are the available departments:\")\n",
        "    for dep in self.list_of_departments:\n",
        "      print(dep.name)\n",
        "    print(\"============================\")\n",
        "\n",
        "  def add_department(self, new_dep_name):\n",
        "    new_dep_instance = Department(new_dep_name, 0)\n",
        "    self.list_of_departments.append(new_dep_instance)\n",
        "\n",
        "\n",
        "  def remove_department (self, old_department):\n",
        "    for dep in self.list_of_departments:\n",
        "      if old_department == dep.name:\n",
        "        self.list_of_departments.remove(dep)\n",
        "\n",
        "\n",
        "  def find_department_by_name(self):\n",
        "    self.show_departments()\n",
        "    user_dep = str(input('choose your department:'))\n",
        "    for dep in self.list_of_departments:\n",
        "      if dep.name == user_dep:\n",
        "        return dep"
      ]
    }
  ]
}