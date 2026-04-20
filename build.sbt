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

    // Auto-generate Scala model from metamodel JSON before compile
    Compile / sourceGenerators += Def.task {
      import scala.sys.process._
      val log = streams.value.log
      val base = baseDirectory.value
      val cmd = Seq("node", (base / "scripts" / "generate-model.js").getPath)
      log.info("Generating info.elect.model from quicksilver-metamodel.json...")
      val rc = Process(cmd, base).!
      if (rc != 0) sys.error("generate-model.js failed")
      // Return the generated .scala files so sbt tracks them
      val modelDir = base / "src" / "main" / "scala" / "info" / "elect" / "model"
      (modelDir ** "*.scala").get
    }.taskValue,

    // Publish to Nexus
    publishTo := Some("Nexus" at "https://repo.elect.info/repository/maven-snapshots/"),
    credentials += Credentials(Path.userHome / ".sbt" / ".credentials")
  )
