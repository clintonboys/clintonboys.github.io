---
layout: post
title: Building iOS apps with React Native
image:
  feature: sample-image-66.jpg
  credit: Entreveux, France, 2022. 
---

Until quite recently I hadn't got around to building a mobile app, but I had a vague idea about the "native" vs "web" debate. In iOS, "native" means the application was built using Swift and UIKit, Apple's APIs and programming language that are deeply linked to the operating system and provide a unified interface across applications, as well as many performance benefits. On Android, which I don't understand quite as well, it seems like Java or Kotlin are usually required to properly write "native" Android apps. Most large software companies will have two separate teams for iOS and Android, and build two separate apps with the different native toolkits. 

On the other end of the spectrum, there are several solutions that allow you to develop from a single code base, and then create builds for both mobile architectures. Usually this involves building a web application, and then compiling it to the native languages, and usually there are some sacrifices: older APIs for compatibility, performance, binary size, etc. The fact that most large companies still have two teams, and are willing to absorb the overhead and cost associated with that, suggest that these sacrifices are usually a little too much if you want truly high quality apps in both ecosystems. 

React Native is a very interesting step in this direction: it lets you write a React web application and then transpile it to native binaries. 

- How mobile applications are usually built
- Description of what React Native is
- Process of creating an app, simplified
- native vs. non native debate
