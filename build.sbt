ThisBuild / organization := "info.elect"
ThisBuild / version := "0.1.0"
ThisBuild / scalaVersion := "2.13.12"

lazy val root = (project in file("."))
  .settings(
    name := "electinfo-common",
    // Include JSON schemas and templates as resources
    Compile / unmanagedResourceDirectories += baseDirectory.value / "schemas",
    Compile / unmanagedResourceDirectories += baseDirectory.value / "templates",
    // Publish to Nexus
    publishTo := Some("Nexus" at "https://repo.elect.info/repository/maven-releases/"),
    credentials += Credentials(Path.userHome / ".sbt" / ".credentials")
  )
