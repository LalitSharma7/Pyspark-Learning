{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPP4PFxkXV4UbfEIEWXhMA2",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/LalitSharma7/Pyspark-Learning/blob/main/Pyspark_rdd1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9hYrhrH4VMHe",
        "outputId": "c9389d6a-3c0c-4eb9-edf6-834f4833fe57"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: pyspark in /usr/local/lib/python3.8/dist-packages (3.3.1)\n",
            "Requirement already satisfied: py4j==0.10.9.5 in /usr/local/lib/python3.8/dist-packages (from pyspark) (0.10.9.5)\n"
          ]
        }
      ],
      "source": [
        "!pip3 install pyspark"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "wndLQmM7Vt_7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from pyspark import SparkContext, SparkConf\n",
        "conf = SparkConf().setAppName(\"TestApp1\").setMaster(\"local[*]\")\n",
        "sc = SparkContext(conf = conf)\n",
        "print(sc)\n",
        "sc.defaultParallelism"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xAhDnt45Vwyw",
        "outputId": "e5c3d347-a78e-4fa4-8c80-9cd9510e0639"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<SparkContext master=local[*] appName=TestApp1>\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "randomlist = random.sample(range(0,90), 10)\n",
        "print(randomlist)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-CjVYCbbWyk3",
        "outputId": "5220e735-75b2-4927-d058-e360f259aa13"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[70, 85, 29, 49, 84, 7, 18, 33, 23, 81]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "rdd1 = sc.parallelize(randomlist, 4)\n",
        "rdd1.collect()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zdESchG4YF1f",
        "outputId": "567b4a37-cc61-461a-ba47-a3b6cd226a50"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[70, 85, 29, 49, 84, 7, 18, 33, 23, 81]"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(rdd1.getNumPartitions())\n",
        "print(rdd1.glom().collect())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VJCcNxzqZC0w",
        "outputId": "4edb292b-682e-4acd-f393-054343bc1a3d"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n",
            "[[70, 85], [29, 49], [84, 7], [18, 33, 23, 81]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "rdd1.glom().collect()[3]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K6ppLPlMZ1Mr",
        "outputId": "5beee2b7-4a36-4161-da55-1ba552fd47f0"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[18, 33, 23, 81]"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "rdd1.count()\n",
        "rdd1.first()\n",
        "\n",
        "# distinct\n",
        "rdd1.distinct().collect()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8mopUIKiZ7e9",
        "outputId": "29b45966-8fb3-4573-fbf5-c8c76370de01"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[84, 85, 29, 49, 33, 81, 70, 18, 7, 23]"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# map\n",
        "# Return a new RDD by applying a function to each element of this RDD\n",
        "def myfunc(item):\n",
        "  return (item+1)*3\n",
        "\n",
        "rdd_map = rdd1.map(myfunc)\n",
        "rdd_map.collect()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B458S4PxaedV",
        "outputId": "cc5caa8c-b221-4c94-e5ef-d9a50fa88d51"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[213, 258, 90, 150, 255, 24, 57, 102, 72, 246]"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# filter\n",
        "# Filter data\n",
        "rdd_filter = rdd1.filter(lambda x: x%3==0)\n",
        "rdd_filter.collect()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qW2N4uwWa-ir",
        "outputId": "826a5a86-a05f-43a0-8493-b56f10e7c661"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[84, 18, 33, 81]"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# flatmap\n",
        "# In a single list\n",
        "rdd_flatmap = rdd1.flatMap(lambda x: [x+2, x+5])\n",
        "rdd_flatmap.collect()\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lVAvMueubLd0",
        "outputId": "7bf8028b-bec5-4e3d-ae44-38554e7eba4b"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[72, 75, 87, 90, 31, 34, 51, 54, 86, 89, 9, 12, 20, 23, 35, 38, 25, 28, 83, 86]"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "rdd_flatmap.reduce(lambda x, y : x+y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TDjx5MRTcAGb",
        "outputId": "18f7f9e9-56ed-4495-8a78-0acf7b314338"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1028"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#descriptive\n",
        "\n",
        "print([rdd1.max(), rdd1.min(), rdd1.mean()])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x_17WZwFcMnb",
        "outputId": "97abdc21-937e-43b4-b2b5-c44d185b7504"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[85, 7, 47.9]\n"
          ]
        }
      ]
    }
  ]
}