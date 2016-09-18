Title: Go beyond in the functionnal paradigm with Javaslang
Date: 2016-09-01 13:09
Tags: java
Slug: javaslang
Author: ihommmani
Summary: How Javaslang allow to bypass some of Java 8 limitations

# Functional paradigm vs Object paradigm
# Java 8 a brand new world

Not so long ago I used to code with Java in a world exclusively dedicated to the Object paradigm. 
Indeed Java 7 was not offering what many languages already were, namely streams and lambdas.  
Then in march 2014 Java 8 was released.
The promise was to open the Java world to functional programming.  
Thanks to the new Stream API and lambdas this was now possible.  
 
However, when comparing Java 8 features with the one provided by pure functional languages (Scala, Haskell)
we still have a gap.  
It appears that Java 8 can still progress into the functional paradigm.  
This is where JavaSlang gets interesting. JavaSlang is a java library developed on top of Java 8 that reimplements some  
of basic data structures (especially collections) to make it fit better the functional paradigm.  
Also with the addition of new data structures, it's an all new world that opens to us. 

In this article I want to give my feedback on JavaSlang's use and show how it can helps in the code expresivity.

# Requirements and Installation
As a library build on top of Java 8, **javaslang requires a JRE 8 to work**.  
Installation is fairly easy, based on the fact you use a build tool like Maven or Gradle.  
Just add a dependency to your project. 
Sources are available on the [github repository](https://github.com/javaslang/javaslang "javaslang").

# Java 8 defects
Once passed the wow effect of the Java 8 stream API. Here what we can complain about:
   
   
*   We have to convert back and forth collections when we want to apply lambda on it

        list.stream().map(...).collect(Collectors.toList())
    Why open a stream instead of applying directly lambdas on the list elements ?

*   Map structure is not well handled by the Stream API

    The way we treat maps through stream is not very intuitive.
        ```
        hashMap.entries.stream().map(entry -> ...)
        ```
    
    Where we would have seen
        ```
        hashMap.entries.stream().map((key, value)-> ... )
        ```

*   Lambdas' inability to throw checked exceptions


# JavaSlang goodness
## Javaslang and the functional paradigm
Using and learning about Javaslang showed me one important thing.  
**Java 8 is not that functional**. It is still deeply rooted in the OO paradigm.    
It allows to apply functionnal patterns with stream and lambda but is not striclty speaking a functional language.    
 
 
So, what is the difference between an OO language and FP language ?

>_FP imposes discipline upon assignment[...]   
>A true functional programming language has no assignment operator. You cannot change the state of a variable._
>Uncle Bob

Yep. It's an all word that opened to my brain washed oriented object mind :)

In OO we mainly expose void methods to modify the state of an object. 
According to Javaslang's creator: 
>_I comprehend a void return type as a smell. It is evidence that side-effects take place, state is mutated.  
Shared mutable state is an important source of failure, not only in a concurrent setting._
>Daniel Dietrich

## How Javaslang does it ?
JavaSlang provides new APIs and data structures to tackle those issues.  
Unlike utilities such as Guava it is not meant to really cohabit with standard Java.  
It replaces it where it needs to. In particular in the implementation of the Java Iterable interface.
This approach gives Javaslang enough liberty to choose immutability over mutability.  
And this gives a true functional flavour to Java. 

## Immutability

Java by default creates mutable data structures, i.e one can operate directly on a structure instance.
```
list.add(3) // list has the 
```
```
map.remove(5) // 
```
Javaslangs' data structures are [persistent](https://en.wikipedia.org/wiki/Persistent_data_structure) and therefore "effectively immutable".  
In short, their operations do not (visibly) update the structure in-place, but instead always yield a new updated structure.  
Do not worry about performance issues, Javaslang share what can be shared :\) .  

This example helped me to understand what it means:  
 

In java we can create a list of three integers as follow.
```
List<Integer> elements = new ArrayList<Integer>  
elements.add(1);  
elements.add(2);  
elements.add(3);    

// elements.size() == 3
```
The add method has no return type (void) and does perform side effect on the list element by adding new elements into it.

In JavaSlang, the same example would be: 
```
List<Integer> elements = List.empty();
elements.push(3).push(2).push(3);
```
```
// If we get elements. It is still empty
// elements.size() == 0 !
```
In fact we have to assign the list returned by push to get the **new** list. 
```
List<String> filledElements = elements.push(3).push(2).push(3);
```

Strange at first, but nice !  
This is the case for all data structures in JavaSlang.

## Functional data structures API
In Java 8 we tend to separate the data collection from the operations.   
That obliges us to open a stream on a list (datas), performs operations on it (stream elements), and then recollect it. 

If we think stream as a lazy list of operations, it is as if we had to clip two lists together to get a refined list.

Wouldn't it be simpler to directly operate on the list instead of a stream ?
Javaslang thinks so. Simpler and more expressive.

```
List<String> toto = List.of("hello", "world").map(operation1).map(operation2);
```
**No more recollection.** 

One of the pain point when working on Map with Java, is the unability to simply parcour map entries.  
In javaSlang this is very easy as the map method accepts a bifunction.  
A rather complex operation in java such as inverting the pair key/value in a Map:
```
// We use a collector with two Functions<String, String>
map.entrySet().stream().collect(Collectors.toMap(Map.Entry::getValue, Map.Entry::getKey)); 
```
Ends up in javaslang with: 
```
// We use one bifunction (Function2<String, String, Tuple2<String, String>>)
map.map((key, value) -> Tuple.of(value, key));
```
## Stream on steroids
Most functional operations on collections do not require to open a stream anymore.  
So in most cases Stream will not be as needed as it is with standard java.   

In fact, in javaSlang we use Streams for what they really are i.e a linked list of operation lazily evaluated and not what they allow to do.
Let's precise this thought. 

In java 8 the vast majority of my Stream API use cases are with collections.  
From a collection (List or Map) I open a stream to aggregate operations and finally consume the stream by collecting the stream element.
Like we saw, in JavaSlang, we directly do this on the List/Map object.
So why do we need streams for ?

1) **Stream are lazily evaluated**  
When collecting operation, you don't need/want to apply it at once (eagerly).  
For instance you may need an element you'll catch later in your execution flow, to apply it in a filter for instance. 

2) **Data contained into a stream can be expressed through logical expressions**  
What if I need to represent all the prime number. Remember, it is infinite :) 
First solution:
```
List.of(1, 3, 5, 7, 11 ....)  // See you at the end of eternity . Anyway your computer has not enough memory.
```
Or:
```
 // = Stream(2L, 3L, 5L, 7L, ...)
 Stream.iterate(2L, PrimeNumbers::nextPrimeFrom)
```
where
```
 // helpers    
 static long nextPrimeFrom(long num)  {  
     return Stream.from(num + 1).find(PrimeNumbers::isPrime).get();  
 }  

 static boolean isPrime(long num) {  
     return !Stream.rangeClosed(2L, (long) Math.sqrt(num)).exists(d -> num % d == 0);  
 }  
```
 
Beautiful, isn't it ?
 
**Streams allow to express a level of abstraction that list structures can't.**  
 
 
So how do I access the processed elements of a stream ? Do we need to collect or do something else ?  
Oddly enough, there is no such thing as Collector in JavaSlang.
In fact, you can directly access the element of a stream.
```
// b
Stream.of("a", "b", "c").get(1)
```

```
// 2
Stream.ofAll(List.of("hello", "world")).size()
```
If you really want to get it into a collection, we can think of: 
```
 HashMap.ofEntries(Stream.of(Tuple.of("key", "value")));
```
or
```
List.ofAll(Stream.of("hello", "world"))
```
 
## Traversables and Seq

Lists, Maps and Streams are all implementations of [Traversable](http://static.javadoc.io/io.javaslang/javaslang/2.0.0/javaslang/collection/Traversable.html) 
and [Seq](http://static.javadoc.io/io.javaslang/javaslang/2.0.0/javaslang/collection/Seq.html) (except Map) interfaces.   
They offer a complete set of methods, we unfortunately don't have in standard Java.  
Here is a few of them, the complete list is to be found on the doc API.  


*   sliding ~ windows function in SQL

*   slicing

*   zip

*   crossProduct

*   dropUntil

I highly suggest to read them all once, so you can have an idea of how you can simplify your existing code using these new methods.

##  New data structures

JavaSlang is also a new set of data

### Tuple
Something we really miss in java. A collection of elements of different types.  
**To use carrefully though**.  It should not replace the notion of class.  

When we come from Java, we tend to see everything as a class.   
So a Tuple can be seen as a class with poor expressiveness since we access its elements  
through standard getters (_1, _2,...,_8) that do not say much on the underlying element.  


What I see in tuples is a "context" factory on the fly. For instance in javaSlang, Maps are list of Tuple2 and not of 'MapEntry' objects... 
It is very handy to use when chaining lambda operations, because it allow to return several outputs packaged into one Tuple.  

```
int inputValue = 42;
listOfvalues.map(value -> Tuple2.of(value, inputValue)).foreach(this::operation);
```
```
void operation(Tuple2<String, int> tuple){
    // make something with tuple._1
    
    // make something with tuple._2
}
```

### Try
In java, lambdas cannot throw checked exceptions.  
Javaslang offers a specific data structure to wrap lambdas that may fail in error.  


### Option
In java8 we have optionals.  
Its constructor, _Optional.of()_ throws an NPE on a null reference (not necessarily a bad thing). To handle null reference we have Optional.ofNullable().   
In javaSlang there is only one constructor _Option.of()_. It is the only real difference I noticed with Java optional.  
In usage we rather use the same pattern than in standard java. 

### Pattern matching
I haven't used this feature much. It is still in development and integration with Intellij is not really that good.  

# Drawbacks
## Naming collision
JavaSlang is a layer above standard Java8 to make it more functional.  
It reimplements many structures.  
The drawback lies in the word "reimplementation".  



Where Guava is more an utility to ease the use of Standard Java and cohabites well with Java,
JavaSlang will struggle to do so.  
Because of naming collision (List and Map for instance), working in the same class with standard java and javaslang is cumbersome.  
When using javaSlang inside a class it has to be isolated and be exclusively used.
That brings us to another drawback.

## Cooperation with other modules
We don't have the control on all the code we work with. Using a tierce SDK for instance.  
Other libraries surely don't use JavaSlang.  
That create contention points where we need to convert a Java util list into a javaSlang list for instance. Same thing for maps and stream.
Although JavaSlang provides utilities such as toJavaList, List.ofAll, this work stay tedious.

## Watch out NullPointerExceptions
Thes transformations are not harmless either.
``` 
javaslangList.toJavaList()
```
```
List.ofAll(javaList)
```
Are as many potential NPE we have to be carefull on.

# Should I consider Java for my code ?
It depends.
 
First of all you need your project to run on Java 8.   
The second and as mandatory condition, the code you modify must be tested hard !  
As far as I am concerned I took the opportunity to modify production code with Javaslang only because of unit tests and
integration tests.   
Forget it on untested legacy code.

If you intend to develop a library you want to share, I would not recommand to add an extra dependency to the library's consumers.   
This [nice article](https://blog.jooq.org/2016/08/11/all-libraries-should-follow-a-zero-dependency-policy/) explain this point of view.

# Conclusion

JavaSlang is really worth the try. It brings java functional development to a more pragmatic level.  
It is also glimpse of what other functional languages offer.  
We have however seen that it comes at a price. Wether you can afford this cost or not should not
detere you from trying it. At least to see what other functional languages offer, in comparaison to Java without having to.
