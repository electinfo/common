ThisBuild / organization := "info.elect"
ThisBuild / version := "0.2.0-SNAPSHOT"
ThisBuild / scalaVersion := "2.13.12"

lazy val sparkVersion = "4.1.0"

lazy val root = (project in file("."))
  .settings(
    name := "electinfo-common",
    // Maven-style source layout
    Compile / unmanagedSourceDirectories := Seq(baseDirectory.value / "src" / "main" / "scala"),
    Test / unmanagedSourceDirectories := Seq(baseDirectory.value / "src" / "test" / "scala"),
    // Include JSON schemas and templates as resources
    Compile / unmanagedResourceDirectories += baseDirectory.value / "schemas",
    Compile / unmanagedResourceDirectories += baseDirectory.value / "templates",

    // Spark SQL types (provided — consumers supply the runtime)
    libraryDependencies ++= Seq(
      "org.apache.spark" %% "spark-sql" % sparkVersion % Provided
    ),

    // Generated Scala model files are committed to git.
    // Freshness is verified by CI via: npm run generate:scala:check
    // To regenerate locally: npm run generate:scala

    // Publish to Nexus
    publishTo := Some("Nexus" at "https://repo.elect.info/repository/maven-snapshots/"),
    credentials += Credentials(Path.userHome / ".sbt" / ".credentials")
  )
