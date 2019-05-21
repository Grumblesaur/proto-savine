#!/usr/bin/python
# -*- coding: utf-8 -*-

from enum import Enum
from random import choice
from random import randint

class C(Enum):
  M     = 'm'; M_DOT = 'mˠ'
  P     = 'p'; P_DOT = 'pˠ'
  B     = 'b'; B_DOT = 'bˠ'
  F     = 'f'; F_DOT = 'fˠ'
  V     = 'v'; V_DOT = 'vˠ'
  N     = 'n'; N_DOT = 'nˠ'
  T     = 't'; T_DOT = 'tˠ'
  D     = 'd'; D_DOT = 'dˠ'
  S     = 'ʃ'; S_DOT = 'sˠ'
  L     = 'l'; L_DOT = 'lˠ'
  R     = 'ɾ'; R_DOT = 'ɾˠ'
  K     = 'k'; K_DOT = 'kʷ'
  G     = 'g'; G_DOT = 'gʷ'
  X     = 'x'; X_DOT = 'xʷ'
  W     = 'ɰ'; W_DOT = 'w'
  H     = 'h'; H_DOT = 'hʷ'
  
class Consonants(Enum):
  M = 'm'; M_DOT = 'ṃ'
  P = 'p'; P_DOT = 'p̣'
  B = 'b'; B_DOT = 'ḅ'
  F = 'f'; F_DOT = 'f̣'
  V = 'v'; V_DOT = 'ṿ'
  N = 'n'; N_DOT = 'ṇ'
  T = 't'; T_DOT = 'ṭ'
  D = 'd'; D_DOT = 'ḍ'
  S = 's'; S_DOT = 'ṣ'
  L = 'l'; L_DOT = 'ḷ'
  R = 'r'; R_DOT = 'ṛ'
  K = 'k'; K_DOT = 'ḳ'
  G = 'g'; G_DOT = 'g̣'
  X = 'x'; X_DOT = 'x̣'
  W = 'w'; W_DOT = 'ẉ'
  H = 'h'; H_DOT = 'ḥ'

class Vowels(Enum):
  HIGH = 'u'
  MID  = 'o'
  LOW  = 'a'


class Type(Enum):
  BOUNDARY = -1
  PLAIN    = 0
  COLORED  = 1


IPA_VOWELS = {
  (Type.COLORED,  Vowels.HIGH, Type.COLORED ) : 'u',
  (Type.COLORED,  Vowels.HIGH, Type.BOUNDARY) : 'u',
  (Type.BOUNDARY, Vowels.HIGH, Type.COLORED ) : 'u',
  (Type.BOUNDARY, Vowels.HIGH, Type.BOUNDARY) : 'i',
  (Type.PLAIN,    Vowels.HIGH, Type.PLAIN   ) : 'i',
  (Type.PLAIN,    Vowels.HIGH, Type.BOUNDARY) : 'i',
  (Type.BOUNDARY, Vowels.HIGH, Type.PLAIN   ) : 'i',
  (Type.COLORED,  Vowels.HIGH, Type.PLAIN   ) : 'ui',
  (Type.PLAIN,    Vowels.HIGH, Type.COLORED ) : 'iu',

  (Type.COLORED,  Vowels.MID,  Type.COLORED ) : 'o',
  (Type.COLORED,  Vowels.MID,  Type.BOUNDARY) : 'o',
  (Type.BOUNDARY, Vowels.MID,  Type.COLORED ) : 'o',
  (Type.BOUNDARY, Vowels.MID,  Type.BOUNDARY) : 'e',
  (Type.PLAIN,    Vowels.MID,  Type.PLAIN   ) : 'e',
  (Type.PLAIN,    Vowels.MID,  Type.BOUNDARY) : 'e',
  (Type.BOUNDARY, Vowels.MID,  Type.PLAIN   ) : 'e',
  (Type.COLORED,  Vowels.MID,  Type.PLAIN   ) : 'oe',
  (Type.PLAIN,    Vowels.MID,  Type.COLORED ) : 'eo',

  (Type.COLORED,  Vowels.LOW,  Type.COLORED ) : 'ɒ',
  (Type.COLORED,  Vowels.LOW,  Type.BOUNDARY) : 'ɒ',
  (Type.BOUNDARY, Vowels.LOW,  Type.COLORED ) : 'ɒ',
  (Type.BOUNDARY, Vowels.LOW,  Type.BOUNDARY) : 'æ',
  (Type.PLAIN,    Vowels.LOW,  Type.PLAIN   ) : 'æ',
  (Type.PLAIN,    Vowels.LOW,  Type.BOUNDARY) : 'æ',
  (Type.BOUNDARY, Vowels.LOW,  Type.PLAIN   ) : 'æ',
  (Type.COLORED,  Vowels.LOW,  Type.PLAIN   ) : 'ɒæ',
  (Type.PLAIN,    Vowels.LOW,  Type.COLORED ) : 'æɒ',
}

VOWELS = {
  Vowels.HIGH : Vowels.HIGH,
  Vowels.MID  : Vowels.MID,
  Vowels.LOW  : Vowels.LOW
}

COLORED = {
  Consonants.M_DOT : C.M_DOT,
  Consonants.P_DOT : C.P_DOT,
  Consonants.B_DOT : C.B_DOT,
  Consonants.F_DOT : C.F_DOT,
  Consonants.V_DOT : C.V_DOT,
  Consonants.N_DOT : C.N_DOT,
  Consonants.T_DOT : C.T_DOT,
  Consonants.D_DOT : C.D_DOT,
  Consonants.S_DOT : C.S_DOT,
  Consonants.L_DOT : C.L_DOT,
  Consonants.R_DOT : C.R_DOT,
  Consonants.K_DOT : C.K_DOT,
  Consonants.G_DOT : C.G_DOT,
  Consonants.X_DOT : C.X_DOT,
  Consonants.W_DOT : C.W_DOT,
  Consonants.H_DOT : C.H_DOT
}

COLORED_OBSTRUENTS = {
  Consonants.P_DOT : C.P_DOT,
  Consonants.B_DOT : C.B_DOT,
  Consonants.F_DOT : C.F_DOT,
  Consonants.V_DOT : C.V_DOT,
  Consonants.T_DOT : C.T_DOT,
  Consonants.D_DOT : C.D_DOT,
  Consonants.S_DOT : C.S_DOT,
  Consonants.K_DOT : C.K_DOT,
  Consonants.G_DOT : C.G_DOT,
  Consonants.X_DOT : C.X_DOT,
}

COLORED_RESONANTS = {
  Consonants.R_DOT : C.R_DOT,
  Consonants.L_DOT : C.L_DOT

}


PLAIN = {
  Consonants.M : C.M,
  Consonants.P : C.P,
  Consonants.B : C.B,
  Consonants.F : C.F,
  Consonants.V : C.V,
  Consonants.N : C.N,
  Consonants.T : C.T,
  Consonants.D : C.D,
  Consonants.S : C.S,
  Consonants.L : C.L,
  Consonants.R : C.R,
  Consonants.K : C.K,
  Consonants.G : C.G,
  Consonants.X : C.X,
  Consonants.W : C.W,
  Consonants.H : C.H
}

PLAIN_OBSTRUENTS = {
  Consonants.P : C.P,
  Consonants.B : C.B,
  Consonants.F : C.F,
  Consonants.V : C.V,
  Consonants.T : C.T,
  Consonants.D : C.D,
  Consonants.S : C.S,
  Consonants.K : C.K,
  Consonants.G : C.G,
  Consonants.X : C.X,
}


PLAIN_RESONANTS = {
  Consonants.R : C.R,
  Consonants.L : C.L
}

CONSONANTS = { }
for key, value in list(COLORED.items()) + list(PLAIN.items()):
  CONSONANTS[key] = value

SYLLABLE_STRUCTURES = (
  (VOWELS,),
  (VOWELS,),
  (CONSONANTS, VOWELS),
  (CONSONANTS, VOWELS),
  (CONSONANTS, VOWELS),
  (CONSONANTS, VOWELS),
  (CONSONANTS, VOWELS),
  (CONSONANTS, VOWELS),
  (CONSONANTS, VOWELS),
  (PLAIN_OBSTRUENTS, PLAIN_RESONANTS, VOWELS),
  (PLAIN_OBSTRUENTS, PLAIN_RESONANTS, VOWELS),
  (PLAIN_OBSTRUENTS, PLAIN_RESONANTS, VOWELS),
  (PLAIN_OBSTRUENTS, PLAIN_RESONANTS, VOWELS),
  (PLAIN_OBSTRUENTS, PLAIN_RESONANTS, VOWELS),
  (COLORED_OBSTRUENTS, COLORED_RESONANTS, VOWELS),
  (COLORED_OBSTRUENTS, COLORED_RESONANTS, VOWELS),
  (COLORED_OBSTRUENTS, COLORED_RESONANTS, VOWELS),
  (COLORED_OBSTRUENTS, COLORED_RESONANTS, VOWELS),
)

def generate_syllable():
  structure = choice(SYLLABLE_STRUCTURES)
  syllable = [ ]
  for phoneme_type in structure:
    key = choice(list(phoneme_type.keys()))
    syllable.append(key)
  return syllable

def generate_word(max_syllables):
  number_of_syllables = randint(1, max_syllables)
  word = [Type.BOUNDARY]
  for i in range(number_of_syllables):
    word += generate_syllable()
  word += [Type.BOUNDARY]
  return word

def generate_orthography(word):
  string = ''
  for c in word:
    try:
      string += c.value
    except Exception as e:
      string += ''
  return string

def generate_pronunciation(word):
  string = ''
  for i in range(1, len(word) - 1):
    if word[i] in CONSONANTS:
      string += CONSONANTS[word[i]].value
    else:
      left, right = word[i-1], word[i+1]
      if left in COLORED:
        left = Type.COLORED
      elif left in PLAIN:
        left = Type.PLAIN
      else:
        left = Type.BOUNDARY
      
      if right in COLORED:
        right = Type.COLORED
      elif right in PLAIN:
        right = Type.PLAIN
      else:
        right = Type.BOUNDARY
      
      string += IPA_VOWELS[(left, word[i], right)]
  return string

def main(*args):
  words  = [generate_word(5) for i in range(50)]
  sounds = map(generate_pronunciation, words)
  words  = map(generate_orthography, words)
  
  for word, sound in zip(words, sounds):
    print(word, ': [%s]' % sound)
  return 0

if __name__ == '__main__':
  import sys
  exit_code = main(*sys.argv)
  sys.exit(exit_code)




