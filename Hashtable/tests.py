""" 
file: tests.py
description: Verify the LinkedHashTable class implementation
"""

__author__ = [ "NAME", "NAME" ]

from linkedhashtable import LinkedHashTable

def print_set( a_set ):
    for word in a_set: # uses the iter method
        print( word, end=" " )
    print()

def test0():
    table = LinkedHashTable( 100 )
    table.add( "to" )
    table.add( "do" )
    table.add( "is" )
    table.add( "to" )
    table.add( "be" )

    print_set( table )

    print( "'to' in table?", table.contains( "to" ) )
    table.remove( "to" )
    print( "'to' in table?", table.contains( "to" ) )

    print_set( table )


if __name__ == '__main__':
    test0()

